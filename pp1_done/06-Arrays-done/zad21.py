arr = [15, 8, 31, 47, 2, 19]
print("existed array:", " ".join(map(str, arr)))



reverse = []
for i in range(len(arr) - 1, -1, -1):
    reverse.append(arr[i])

print("reverse array:", " ".join(map(str, reverse)))