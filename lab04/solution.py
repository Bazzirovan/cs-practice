def find_winner(names, scores):
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





if __name__ == __main__:
    #
