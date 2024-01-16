results = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]

def min_pts(limit):
    return list(filter(lambda pts: pts>=limit, results))

a = min_pts(70)
b = min_pts(40)
c = min_pts(30)

print("Min 70 pts:", a)
print("Min 40 pts:", b)
print("Min 30 pts:", c)