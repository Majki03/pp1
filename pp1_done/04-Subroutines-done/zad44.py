def f(password):
    count = 0
    unique = set()

    for i in password:
        if(i not in unique):
            count += 1
            unique.add(i)

    return count >= 6

result1 = f("ax15")
result2 = f("book123")
result3 = f("A2water3")
result4 = f("qwerty")
result5 = f("")

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)