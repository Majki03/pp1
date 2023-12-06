arr = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]

for col in arr:
    print(" ".join(map(str, col)))

swap = arr[0]

arr[0] = arr[2]
arr[2] = swap

print("")

for col in arr:
    print(" ".join(map(str, col)))