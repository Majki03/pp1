li = [2, 3, 7, 5, 4]

a = li
b = len(li)
c = li[0]
d = li[1]
e = li[-1]
f = li[4]
g = li[0] + li[-1]
h = len(li) // 2

print("Array:", a)
print("No. of elemenmts:", b)
print("First value:", c)
print("Second value:", d)
print("Last value:", e)
print("Last value (without negative index):", f)
print("Sum of the first and last value:", g)
print("Middle:", h)
for i in li:
    print(i, end=" ")