arr = [2, 3, 2, 5, 8, 1, 9, 8]
print("Array:", " ".join(map(str, arr)))

unique = [i for i in arr if arr.count(i) == 1]
print("Unique elements:", " ".join(map(str, unique)))