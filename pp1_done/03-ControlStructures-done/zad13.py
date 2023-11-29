num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if(num1 >= 0 or num2 >= 0):
    print(f"At least one of the entered numbers {num1} and {num2} is not negative")
else:
    print("Both of the numbers are negative")