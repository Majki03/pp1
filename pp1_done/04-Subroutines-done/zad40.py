def f(number):
    sum = 0
    for i in str(number):
        if(str(number).count(i) > 1):
            sum += int(i)
    return sum

result1 = f(1027)
result2 = f(230335)
result3 = f(513553007)

print(result1)
print(result2)
print(result3)