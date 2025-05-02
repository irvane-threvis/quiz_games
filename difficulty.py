def get_difficulty_settings(level):
    if level == "easy":
        return {"score_bonus": 1}
    elif level == "medium":
        return {"score_bonus": 1}
    elif level == "hard":
        return {"score_bonus": 1}
    else:
        return {"score_bonus": 0}
