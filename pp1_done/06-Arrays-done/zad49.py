arr = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = (i + 1) * (j + 1)

for row in arr:
    print(' '.join(map(str, row)))