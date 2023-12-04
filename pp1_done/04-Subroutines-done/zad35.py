def f(number1, number2, operator):
    if(operator == "+"):
        suma = number1 + number2
        return suma
    elif(operator == "%"):
        mod = number1 % number2
        return mod
    elif(operator == "**"):
        powe = number1**number2
        return powe
    elif(operator == "*"):
        multi = number1 * number2
        return multi
    elif(operator == "-"):
        sub = number1 - number2
        return sub
    
result1 = f(2, 3, "+")
result2 = f(2, 3, "%")
result3 = f(2, 3, "**")
result4 = f(2, 3, "*")
result5 = f(2, 3, "-")

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)