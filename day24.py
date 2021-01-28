import re

grouprgx = re.compile(r"([0-9]+) units each with ([0-9]+) hit points (.*)with an attack that does ([0-9]+) ([a-z]+) damage at initiative ([0-9]+)")

def buildteam(teamspec):
    groups = []
    for line in teamspec.split("\n"):
        m = grouprgx.match(line)
        if not m:
            continue
        nunits = int(m.group(1))
        hp = int(m.group(2))
        damage = int(m.group(4))
        damtype = m.group(5)
        initiative = int(m.group(6))
        weak = []
        immune = []
        if m.group(3):
            modifiers = [modset.strip() for modset in m.group(3).strip(" )(").split(";")]
            for modset in modifiers:
                if modset.startswith("weak to "):
                    weak = [x.strip() for x in modset[8:].split(",")]
                else:
                    immune = [x.strip() for x in modset[10:].split(",")]
        groups.append((nunits, hp, damage, damtype, initiative, weak, immune))
    return groups

with open("input24.txt") as f:
    battlespec = f.read()

teamspecs = battlespec.split("\n\n")

reindeerlost = True
boost = 42
while reindeerlost:
    teams = list(map(buildteam, teamspecs))
    for gi, group in enumerate(teams[0]):
        teams[0][gi] = (*group[0:2], group[2] + boost, *group[3:])
    stalemate = False
    while all(teams) and not stalemate:
        stalemate = True
        #sort into target selection order (by effective power, tie broken by initiative)
        for team in teams:
            team.sort(key=lambda x: (x[0]*x[2], x[4]), reverse = True)
        #select
        targeting = []
        selected = [[False for group in team] for team in teams]
        for i, team in enumerate(teams):
            grouptargets = []
            for group in team:
                maxdmg = -1
                maxind = -1
                defaultdmg = group[0]*group[2]
                for j, g2 in enumerate(teams[1-i]):
                    if selected[1-i][j]:
                        continue
                    dmg = 0
                    if group[3] in g2[5]:
                        dmg = 2 * defaultdmg
                    elif group[3] not in g2[6]:
                        dmg = defaultdmg
                    if dmg > maxdmg:
                        maxdmg = dmg
                        maxind = j
                    elif dmg == maxdmg:
                        curtgt = teams[1-i][maxind]
                        if g2[0]*g2[2] > curtgt[0]*curtgt[2]:
                            maxind = j
                        elif g2[0]*g2[2] == curtgt[0]*curtgt[2] and g2[4] > curtgt[4]:
                            maxind = j
                if maxdmg <= 0:
                    grouptargets.append(-1)
                else:
                    grouptargets.append(maxind)
                    selected[1-i][maxind] = True
            targeting.append(grouptargets)

        #attack
        #determine turn order
        indices = [(1*(i >= len(teams[0])), i - len(teams[0]) * (i >= len(teams[0]))) for i in range(len(teams[0]) + len(teams[1]))]
        indices.sort(key = lambda idx: teams[idx[0]][idx[1]][4], reverse = True)
        dead = [[False for group in team] for team in teams]
        for teami, groupi in indices:
            if dead[teami][groupi]:
                continue
            tgti = targeting[teami][groupi]
            group = teams[teami][groupi]
            dmg = group[0]*group[2]
            if tgti >= 0:
                tgt = teams[1-teami][tgti]
                if group[3] in tgt[5]:
                    dmg *= 2
                nalive = tgt[0] - dmg // tgt[1]
                if nalive != tgt[0]:
                    stalemate = False
                teams[1-teami][tgti] = (nalive, *tgt[1:])
                if nalive <= 0:
                    dead[1-teami][tgti] = True

        #resolve combat/prune
        nexteams = []
        for teami, team in enumerate(teams):
            nexteam = []
            for groupi, group in enumerate(team):
                if not dead[teami][groupi]:
                    nexteam.append(group)
            nexteams.append(nexteam)
        teams = nexteams
    if teams[0] and not stalemate:
        reindeerlost = False
    else:
        boost += 1

print(sum(sum(group[0] for group in team) for team in teams), boost)