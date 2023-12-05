arr = [[1, 3, 5], [8, 7, 2]]

a = arr[0][0] + arr[-1][-1]
middle_c = len(arr[0]) // 2
b = arr[0][middle_c] + arr[1][middle_c]
c = sum(arr[-1])

print(a)
print(b)
print(c)