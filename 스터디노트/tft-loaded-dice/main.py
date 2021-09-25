import json
from collections import Counter, defaultdict
from pathlib import Path

here = Path(__file__).resolve().parent

LEVEL_ODDS = {
    1: {1: 100, 2: 0, 3: 0, 4: 0, 5: 0},
    2: {1: 100, 2: 0, 3: 0, 4: 0, 5: 0},
    3: {1: 75, 2: 25, 3: 0, 4: 0, 5: 0},
    4: {1: 55, 2: 30, 3: 15, 4: 0, 5: 0},
    5: {1: 45, 2: 33, 3: 20, 4: 2, 5: 0},
    6: {1: 25, 2: 40, 3: 30, 4: 5, 5: 0},
    7: {1: 19, 2: 30, 3: 35, 4: 15, 5: 1},
    8: {1: 15, 2: 20, 3: 35, 4: 25, 5: 5},
    9: {1: 10, 2: 15, 3: 30, 4: 30, 5: 15},
}

with open(here / "champions.json") as f:
    champions_data = json.load(f)

champions_data = {
    c["name"]: {
        "cost": c["cost"],
        "traits": c["traits"],
    }
    for c in champions_data
}

traits_to_units = defaultdict(list)
for c, v in champions_data.items():
    for t in v["traits"]:
        traits_to_units[t].append(c)


def champion_odds(champion):
    if champion not in champions_data:
        print(f"{champion} not found")
    result = {}
    potential_units = _potential_units(champion)
    for unit in potential_units:
        unit_odds = {}
        potential_rerolled = Counter(
            champions_data[c]["cost"] for c in _potential_units(unit)
        )
        #for level in range(3, 9 + 1):
        print(unit)
        for level in range(7,8):
            num = den = 0
            for cost in range(1, 5 + 1):
                if cost == champions_data[champion]["cost"]:
                    num += LEVEL_ODDS[level][cost] / potential_rerolled[cost]
                    print(f"cost : {cost}, num : {num}")
                if potential_rerolled[cost]:
                    den += LEVEL_ODDS[level][cost]
                    print(f"cost : {cost}, den : {den}")
            unit_odds[level] = num / den if den > 0 else 0
        result[unit] = unit_odds
    return result


def best_champions(champion, level):
    odds = champion_odds(champion)
    odds = [(c, odds[c][level]) for c in odds]
    return sorted(odds, key=lambda x: -x[1])


def _potential_units(champion):
    return {
        c
        for trait in champions_data[champion]["traits"]
        for c in traits_to_units[trait]
    }

print(champion_odds("Garen"))
