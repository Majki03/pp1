def f(dice):
    count = 1
    max_count = 0
    for i in range(1, len(dice)):
        if(dice[i] == dice[i - 1]):
            count += 1
        else:
            if(count > max_count):
                max_count = count
                digit = dice[i - 1]
            count = 1
    
    if(count > max_count):
        max_count = count
        digit = dice[i - 1]

    return digit

result1 = f("5233165554211")
result2 = f("2133")

print(result1)
print(result2)