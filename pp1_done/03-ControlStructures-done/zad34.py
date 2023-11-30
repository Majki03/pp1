amount = int(input("Enter the amount in PLN: "))

count_5 = amount // 5
amount %= 5
count_2 = amount // 2
amount %= 2
count_1 = amount

print("The amount of PLN 18 in coins:")
print("5 zł -", count_5)
print("2 zł -", count_2)
print("1 zł -", count_1)