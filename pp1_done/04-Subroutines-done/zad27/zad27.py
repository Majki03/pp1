import mask

number = str(mask.card_number)
result = f"{number[:2]}{mask.f(number)}{number[-4:]}"

print(result)