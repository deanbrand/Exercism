def tally(rows):
    init_table = ["Team                           | MP |  W |  D |  L |  P"]
    final = []
    outcome = {}
    teams = []
    for row in rows:
        res = row.split(";")
        teams.append(res[0])
        teams.append(res[1])

    teams = sorted(set(teams))

    for team in teams:
        outcome[team] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

    for row in rows:
        res = row.split(";")

        outcome[res[0]]["MP"] += 1
        outcome[res[1]]["MP"] += 1

        if res[2] == "win":
            outcome[res[0]]["W"] += 1
            outcome[res[0]]["P"] += 3
            outcome[res[1]]["L"] += 1

        if res[2] == "draw":
            outcome[res[0]]["D"] += 1
            outcome[res[0]]["P"] += 1
            outcome[res[1]]["D"] += 1
            outcome[res[1]]["P"] += 1

        if res[2] == "loss":
            outcome[res[1]]["W"] += 1
            outcome[res[1]]["P"] += 3
            outcome[res[0]]["L"] += 1

    for team in outcome:
        mp = outcome[team]["MP"]
        w = outcome[team]["W"]
        d = outcome[team]["D"]
        l = outcome[team]["L"]
        p = outcome[team]["P"]
        final.append(team + " " * (31 - len(team)) + f"|  {mp} |  {w} |  {d} |  {l} |{' ' * (3 - len(str(p)))}{p}")

    init_table += sorted(final, reverse=True, key=lambda x: int(x[-2:]))

    return init_table
