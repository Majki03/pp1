num = list(range(1, 21))

div23 = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, num))

print(div23)