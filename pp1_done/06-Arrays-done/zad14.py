arr = [[2, 5, 4], [9, 0, 3]]

a = arr
num_rows = len(arr)
num_cols = len(arr[0])
c = arr[0][1]
d = arr[1][2]

print(a)
print(num_rows, num_cols)
print(c)
print(d)
for i in arr[1]:
    print(i, end=" ")