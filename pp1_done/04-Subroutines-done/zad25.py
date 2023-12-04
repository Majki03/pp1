num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

compare = lambda x, y: True if x > y else False

result = compare(num1, num2)

print(result)