arr = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]

for row in arr:
    print(" ".join(map(str, row)))

for row in arr:
    row[0], row[-1] = row[-1], row[0]

print("")

for row in arr:
    print(" ".join(map(str, row)))