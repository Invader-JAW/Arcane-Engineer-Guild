#!/usr/bin/env python3
import argparse, json, shutil, sys
from datetime import datetime
from pathlib import Path

RANKS={0:"Untrained",1:"Apprentice",2:"Initiate",3:"Adept",4:"Specialist",5:"Expert",6:"Master",7:"Grandmaster",8:"Archmage",9:"Legendary",10:"Mythic"}
TH={1:0,2:100,3:250,4:450,5:700,6:1000,7:1350,8:1750,9:2200,10:2700}

def threshold(level):
    return TH[level] if level <= 10 else TH[10] + (level-10)*500

def level_for_xp(xp):
    level=1
    while xp >= threshold(level+1):
        level += 1
    return level

def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def save(path,data):
    tmp=path.with_suffix(path.suffix+".tmp")
    tmp.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    tmp.replace(path)

def validate(e):
    for k in ("schema_version","event_id","date","quest_type","quest_name","xp"):
        if k not in e: raise ValueError(f"Missing {k}")
    if e["schema_version"] != 1: raise ValueError("Unsupported schema_version")
    if not isinstance(e["xp"],int) or e["xp"] < 0: raise ValueError("xp must be a non-negative integer")
    datetime.strptime(e["date"],"%Y-%m-%d")

def unique_add(dst,items):
    names={x["name"] for x in dst}
    for x in items:
        if x["name"] not in names:
            dst.append(x); names.add(x["name"])

def apply(state,e):
    if e["event_id"] in state["processed_event_ids"]:
        return False
    state["character"]["total_xp"] += e.get("xp",0)
    for k,v in e.get("stat_deltas",{}).items():
        state["stats"][k]=state["stats"].get(k,0)+v
    for name,u in e.get("skill_updates",{}).items():
        s=state["skills"].setdefault(name,{"level":0,"evidence":""})
        s["level"]=max(0,min(10,s.get("level",0)+int(u.get("level_delta",0))))
        if u.get("evidence"):
            old=s.get("evidence","")
            if u["evidence"] not in old:
                s["evidence"]=(old+"; "+u["evidence"]).strip("; ")
    for guild,delta in e.get("reputation_deltas",{}).items():
        g=state["guild_reputation"].setdefault(guild,{"rank":"Initiate","points":0})
        g["points"] += int(delta)
    unique_add(state["achievements"],e.get("achievements",[]))
    unique_add(state["inventory"],e.get("items",[]))
    for t in state.get("achievement_trackers",[]):
        if t["name"] in e.get("achievement_progress",{}):
            t["current"]=min(t["target"],t["current"]+int(e["achievement_progress"][t["name"]]))
    state["processed_event_ids"].append(e["event_id"])
    state["character"]["last_event"]={"date":e["date"],"quest_name":e["quest_name"],"xp":e["xp"],"summary":e.get("summary","")}
    return True

def render(state,repo):
    c=state["character"]; xp=c["total_xp"]; lvl=level_for_xp(xp)
    lines=["# Arcane Engineer Character Sheet","",
        f"**Name:** {c['name']}  ",f"**Class:** {c['class']}  ",f"**Subclass:** {c['subclass']}  ",
        f"**Level:** {lvl}  ",f"**Total XP:** {xp}  ",f"**XP Progress:** {xp} / {threshold(lvl+1)}  ",
        f"**Campaign:** {c['campaign']}  ","","## Primary Stats","","| Stat | Score |","|---|---:|"]
    for k,v in state["stats"].items(): lines.append(f"| {k} | {v:g} |" if isinstance(v,float) else f"| {k} | {v} |")
    lines+=["","## Guild Reputation","","| Guild | Rank | Points |","|---|---|---:|"]
    for k,v in state["guild_reputation"].items(): lines.append(f"| {k} | {v['rank']} | {v['points']} |")
    lines+=["","## Current Quest","",c.get("current_quest","Awaiting quest."),"","## Latest System Event",""]
    le=c.get("last_event")
    lines += ([f"**{le['date']} — {le['quest_name']}**  ",f"+{le['xp']} XP  ",le.get("summary","")] if le else ["No processed events yet."])
    (repo/"Character/Character-Sheet.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

    a=["# Achievements","","## Unlocked",""]
    for x in state["achievements"]:
        a += [f"### 🏆 {x['name']}","",f"**Date unlocked:** {x.get('date','')}  ",f"**Quest:** {x.get('quest','')}  ",f"**Reward:** {x.get('reward','')}  ","",x.get("description",""),""]
    a += ["## In Progress","","| Achievement | Requirement | Progress |","|---|---|---:|"]
    for t in state.get("achievement_trackers",[]): a.append(f"| {t['name']} | {t['requirement']} | {t['current']} / {t['target']} |")
    (repo/"Character/Achievements.md").write_text("\n".join(a)+"\n",encoding="utf-8")

    inv=["# Inventory","","## Permanent Items",""]
    for x in state["inventory"]:
        inv += [f"### 🎒 {x['name']}","",f"**Date acquired:** {x.get('date','')}  ",f"**Quest or milestone:** {x.get('quest','')}  ",f"**Rarity:** {x.get('rarity','')}  ",f"**Related skill:** {x.get('related_skill','')}  ","",x.get("meaning",""),""]
    (repo/"Character/Inventory.md").write_text("\n".join(inv)+"\n",encoding="utf-8")

    sk=["# Skill Trees","","Skill levels represent demonstrated ability.","","| Skill | Level | Rank | Evidence |","|---|---:|---|---|"]
    for name in sorted(state["skills"]):
        d=state["skills"][name]; lv=int(d.get("level",0))
        sk.append(f"| {name} | {lv} | {RANKS.get(lv,'Mythic')} | {d.get('evidence','—')} |")
    (repo/"Character/Skill-Trees.md").write_text("\n".join(sk)+"\n",encoding="utf-8")

def log_event(e,path):
    path.parent.mkdir(parents=True,exist_ok=True)
    lines=[f"## {e['date']} — {e['quest_name']}","",f"**Type:** {e['quest_type']}  ",f"**XP:** +{e['xp']}  ","",e.get("summary",""),""]
    if e.get("evidence"): lines += ["### Evidence",""]+[f"- {x}" for x in e["evidence"]]+[""]
    with path.open("a",encoding="utf-8") as f: f.write("\n".join(lines)+"\n")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",default="."); ap.add_argument("--render-only",action="store_true"); args=ap.parse_args()
    repo=Path(args.repo).resolve(); state_path=repo/"Data/character-state.json"; state=load(state_path)
    inbox=repo/"System/Inbox"; processed=repo/"System/Processed"; rejected=repo/"System/Rejected"
    processed.mkdir(parents=True,exist_ok=True); rejected.mkdir(parents=True,exist_ok=True)
    if not args.render_only:
        for p in sorted(inbox.glob("*.json")):
            if p.name.startswith("EXAMPLE-"): continue
            try:
                e=load(p); validate(e)
                if apply(state,e):
                    log_event(e,repo/"Journal/System-Event-Log.md")
                    print(f"APPLIED {e['event_id']} (+{e['xp']} XP)")
                else:
                    print(f"SKIPPED duplicate {e['event_id']}")
                shutil.move(str(p),str(processed/p.name))
            except Exception as ex:
                print(f"REJECTED {p.name}: {ex}",file=sys.stderr)
                shutil.move(str(p),str(rejected/p.name))
    render(state,repo); save(state_path,state)
    print(f"Level {level_for_xp(state['character']['total_xp'])} — {state['character']['total_xp']} XP")

if __name__=="__main__":
    main()
