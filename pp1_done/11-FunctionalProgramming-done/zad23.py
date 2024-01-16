rate = [(17, 15, 16, 17, 15),
        (16, 18, 19, 17, 19),
        (19, 15, 15, 19, 18),
        (18, 17, 19, 15, 16)]

def cal(scores):
    return sum(scores) - min(scores) - max(scores)

score = list(map(cal, rate))

print(score)