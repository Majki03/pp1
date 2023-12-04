def f(x, y):
    sum = 0
    for i in range(x, y + 1):
        if(i % 2 == 0 and i % 3 == 0 and i % 4 != 0):
            sum += i
    return sum

result1 = f(1, 20)
result2 = f(10, 30)

print(result1)
print(result2)