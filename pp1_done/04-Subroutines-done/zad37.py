def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

result1 = f(5)
result2 = f(9)

print(result1)
print(result2)