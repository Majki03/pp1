number = int(input("Enter number: "))


if(number < 0):
    absolute = number * (-1)
    print(f"|{number}| = {absolute}")
else:
    print(f"|{number}| = {number}")