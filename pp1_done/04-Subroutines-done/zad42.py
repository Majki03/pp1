def f(number1, number2, number3):
    max_num = max(number1, number2, number3)
    min_num = min(number1, number2, number3)

    diff = max_num - min_num

    return diff

result1 = f(7, 4, 9)
result2 = f(2, 12, 8)

print(result1)
print(result2)