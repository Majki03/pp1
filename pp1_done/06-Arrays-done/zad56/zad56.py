import convert

a = [[2, 3], [1, 5]]
b = [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]
c = [[2, 1], [3, 5], [7, 4], [2, 6]]

con_a = convert.converet(a)
con_b = convert.converet(b)
con_c = convert.converet(c)

print(" ".join(map(str, con_a)))
print(" ".join(map(str, con_b)))
print(" ".join(map(str, con_c)))