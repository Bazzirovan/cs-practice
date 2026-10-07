def winner(names: list[str], scores: list[float]) -> str:
    n = names.copy()
    s = scores.copy()
    if not names:
        return ""
    max_i = 0
    max_score = 0
    for i in scores:
        if scores[i] > max_score:
            max_score = scores[i]
            max_i = i
    return max_i


def average(scores: list[float]) -> float:
    if not scores: return 0.0
    return round(sum(scores) / len(scores), 2)






if __name__ == __main__:
    #
