def f(n):
    for i in range(n + 1):
        result = ("*" + "/") * i
    return result

result1 = f(4)
result2 = f(1)

print(str(result1[:-1]))
print(str(result2[:-1]))