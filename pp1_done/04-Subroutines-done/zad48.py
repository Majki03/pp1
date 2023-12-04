def f(product_code):
    crop = "+".join(product_code[:3])
    sum = eval(crop)
    rem = sum % 7
    rm = eval(product_code[-1:])

    if(rem == rm):
        return True
    else:
        return False

result1 = f("1082")
result2 = f("2035")
result3 = f("1114")
result4 = f("7071")

print(result1)
print(result2)
print(result3)
print(result4)