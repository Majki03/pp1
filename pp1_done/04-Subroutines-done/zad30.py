def f(number, even):
    digits = [int(digit) for digit in str(number)]
    
    if even:
        filtered_digits = filter(lambda x: x % 2 == 0, digits)
    else:
        filtered_digits = filter(lambda x: x % 2 != 0, digits)
    
    return sum(filtered_digits)
    
result1 = f(3124, True)
result2 = f(3124, False)
result3 = f(20576, False)
result4 = f(20576, True)
result5 = f(13115, True)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)