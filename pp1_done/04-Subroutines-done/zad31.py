def f(x, y):
    sum = 0
    for i in range(x, y):
        if(i < 0 and i % 2 == 0):
            sum += 1
    return sum

result1 = f(-7, 8)
result2 = f(-1, 11)

print(result1)
print(result2)