#!/usr/bin/env python3
from pathlib import Path
import json

RANKS={0:"Untrained",1:"Apprentice",2:"Initiate",3:"Adept",4:"Specialist",5:"Expert",6:"Master",7:"Grandmaster",8:"Archmage",9:"Legendary",10:"Mythic"}
TH={1:0,2:100,3:250,4:450,5:700,6:1000,7:1350,8:1750,9:2200,10:2700}

def threshold(level):
    return TH[level] if level <= 10 else TH[10] + (level-10)*500

def level_for_xp(xp):
    level=1
    while xp >= threshold(level+1):
        level += 1
    return level

def bar(value,maximum,width=18):
    ratio=0 if maximum<=0 else max(0,min(1,value/maximum))
    filled=round(ratio*width)
    return "█"*filled+"░"*(width-filled)

def save(path, lines):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text("\n".join(lines).rstrip()+"\n",encoding="utf-8")

def main():
    repo=Path(__file__).resolve().parents[1]
    s=json.loads((repo/"Data/character-state.json").read_text(encoding="utf-8-sig"))
    c=s["character"]; xp=c["total_xp"]; lvl=level_for_xp(xp); nxt=threshold(lvl+1); floor=threshold(lvl)

    # Character Sheet
    lines=[
        "# 🧙 Arcane Engineer","",
        "> *The System recognizes all progress backed by real evidence.*","",
        "```text",
        "═══════════════════════════════════════",
        "              STATUS SCREEN",
        "═══════════════════════════════════════",
        f"Name       {c['name']}",
        f"Class      {c['class']}",
        f"Subclass   {c['subclass']}",
        f"Level      {lvl}",
        f"XP         {xp} / {nxt}",
        f"Progress   {bar(xp-floor,nxt-floor)}",
        f"Campaign   {c['campaign']}",
        "═══════════════════════════════════════",
        "```","",
        "## 📊 Primary Stats","",
        "| Attribute | Score | Status |","|---|---:|---|"
    ]
    icons={"Intellect":"🧠","Wisdom":"📚","Charisma":"🗣️","Creativity":"🎨","Engineering":"⚙️","Automation":"⚡","Leadership":"👑"}
    for k,v in s["stats"].items():
        lines.append(f"| {icons.get(k,'✦')} **{k}** | **{v}** | `{bar(float(v),20,10)}` |")
    lines += ["","## ⭐ Guild Reputation","","| Guild | Rank | Reputation |","|---|---|---:|"]
    for k,v in s["guild_reputation"].items():
        lines.append(f"| **{k}** | {v['rank']} | {v['points']} |")
    lines += ["","## ⚔ Current Quest","",f"> {c.get('current_quest','Awaiting the System.')}","",
              "## 🕯 Latest System Event",""]
    le=c.get("last_event")
    lines += ([f"### {le['date']} — {le['quest_name']}","",f"**Reward:** +{le['xp']} XP  ","",le.get("summary","")] if le else ["> No processed event yet."])
    save(repo/"Character/Character-Sheet.md",lines)

    # Achievements
    a=["# 🏆 Achievements","","> *Every achievement represents real evidence from the journey.*","","## ✨ Unlocked",""]
    for x in s.get("achievements",[]):
        a += [f"### 🏆 {x['name']}","",f"> {x.get('description','')}","",
              f"**Unlocked:** {x.get('date','Unknown')}  ",f"**Quest:** {x.get('quest','Unknown')}  ",
              f"**Reward:** {x.get('reward','—')}  ","","---",""]
    a += ["## 🔒 Achievement Progress","","| Achievement | Progress | Requirement |","|---|---:|---|"]
    for t in s.get("achievement_trackers",[]):
        a.append(f"| **{t['name']}** | `{bar(t['current'],t['target'],10)}` {t['current']}/{t['target']} | {t['requirement']} |")
    save(repo/"Character/Achievements.md",a)

    # Inventory
    inv=["# 🎒 Inventory","","> *Artifacts mark milestones earned through real progress.*","","## ✨ Permanent Artifacts",""]
    rarity_icon={"Legendary":"🟠","Epic":"🟣","Rare":"🔵","Uncommon":"🟢","Common":"⚪"}
    for x in s.get("inventory",[]):
        rarity=x.get("rarity","Common")
        inv += [f"## {rarity_icon.get(rarity,'✦')} {x['name']}","",
                f"**Rarity:** `{rarity.upper()}`  ",f"**Acquired:** {x.get('date','Unknown')}  ",
                f"**Milestone:** {x.get('quest','Unknown')}  ",f"**Related Skill:** {x.get('related_skill','—')}  ","",
                f"> *{x.get('meaning','')}*","","---",""]
    save(repo/"Character/Inventory.md",inv)

    # Skills
    sk=["# 🌲 Skill Trees","","> *Skill ranks reflect demonstrated ability.*","",
        "| Skill | Rank | Level | Mastery | Evidence |","|---|---|---:|---|---|"]
    for name in sorted(s.get("skills",{})):
        d=s["skills"][name]; lv=int(d.get("level",0))
        sk.append(f"| **{name}** | {RANKS.get(lv,'Mythic')} | {lv} | `{bar(lv,10,10)}` | {d.get('evidence','—')} |")
    save(repo/"Character/Skill-Trees.md",sk)

    # Titles
    unlocked=[x for x in s.get("achievements",[]) if x["name"] in ("Guild Founder","World Builder")]
    titles=["# 🏷 Titles","","> *Titles commemorate major milestones earned during the campaign.*","","## Equipped",""]
    titles += ([f"### ✨ {unlocked[0]['name']}","",f"> {unlocked[0].get('description','')}",""] if unlocked else ["> No title equipped.",""])
    titles += ["## Unlocked",""]+[f"- 🏷 **{x['name']}** — {x.get('date','Unknown')}" for x in unlocked]
    titles += ["","## Future Titles","","- 🔒 Container Adept","- 🔒 Reliability Guardian","- 🔒 Automation Sage","- 🔒 Wizard Merchant","- 🔒 Senior DevOps Engineer","- 🔒 Site Reliability Engineer","- 🔒 Arcane Archmage"]
    save(repo/"Character/Titles.md",titles)

    # Reputation
    rep=["# ⭐ Guild Reputation","","> *Reputation measures visible real-world progress with each guild.*",""]
    for name,d in s.get("guild_reputation",{}).items():
        rep += [f"## {name}","",f"**Current Rank:** {d['rank']}  ",f"**Reputation:** {d['points']}  ","",f"`{bar(d['points'],50,20)}`",""]
    save(repo/"Character/Guild-Reputation.md",rep)

    # Dashboard
    dash=["# 🏰 Guild Hall","","> **Continue Campaign**","",
          f"## 🧙 {c['name']} — Level {lvl} {c['subclass']}","",
          f"**XP:** {xp} / {nxt}  ",f"`{bar(xp-floor,nxt-floor,24)}`","",
          "## 🗺 Campaign Menu","",
          "- [[Character/Character-Sheet|🧙 Character Sheet]]",
          "- [[Character/Achievements|🏆 Achievements]]",
          "- [[Character/Inventory|🎒 Inventory]]",
          "- [[Character/Skill-Trees|🌲 Skill Trees]]",
          "- [[Character/Titles|🏷 Titles]]",
          "- [[Character/Guild-Reputation|⭐ Guild Reputation]]",
          "- [[Journal/System-Event-Log|📜 System Event Log]]",
          "- [[SYSTEM|⚙ System Rules]]","",
          "## ⚔ Current Quest","",f"> {c.get('current_quest','Awaiting the System.')}","",
          "## 🎯 Primary Paths","","- ⚙️ **Senior DevOps / SRE**","- 🧶 **The Wizard Who Crochets**"]
    save(repo/"Guild-Hall.md",dash)
    print("Rendered immersive LitRPG views.")

if __name__=="__main__":
    main()
