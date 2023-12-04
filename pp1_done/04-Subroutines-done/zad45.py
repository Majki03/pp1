def f(expression):
    return eval(expression)

result1 = f("2 + 3")
result2 = f("3 + 8 + 1")
result3 = f("2 + 3 - 4 + 5 - 0")

print(result1)
print(result2)
print(result3)