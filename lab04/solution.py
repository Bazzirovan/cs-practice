def winner(names, scores):
    n = names.copy()
    s = scores.copy()
    if not names:
        return ""
    max_i = 0
    max_score = float("-inf")
    for i in range(len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            max_i = i
    return names[max_i]


def average(scores):
    if not scores: return 0.0
    return round(sum(scores) / len(scores), 2)


def ranking(names, scores):
    ind = list(range(len(names)))
    ind.sort(key = lambda i: scores[i], reverse = True)

    return [names[i] for i in ind]


def above_average(names, scores):
    avg = average(scores)
    return [names[i] for i in range(len(names)) if scores[i] > avg]

    #

if __name__ == "__main__":
    test_names = ["Аня", "Боря", "Вика"]
    test_scores = [7.0, 9.0, 9.0]

    print(winner(test_names, test_scores))
