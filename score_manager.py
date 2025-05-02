import json
import os

def save_score(player_name, level, score):
    if not os.path.exists("data/scores.json"):
        with open("data/scores.json", "w") as f:
            json.dump([], f)

    with open("data/scores.json", "r") as f:
        try:
            scores = json.load(f)
            if not isinstance(scores, list):
                scores = []
        except json.JSONDecodeError:
            scores = []

    scores.append({
        "player": player_name,
        "level": level,
        "score": score
    })

    with open("data/scores.json", "w") as f:
        json.dump(scores, f, indent=4)
