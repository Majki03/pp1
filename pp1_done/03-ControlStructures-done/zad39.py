a = int(input("Enter a: "))
b = int(input("Enter b: "))

top = "*" * b

side = " " * (b - 2)
sides = (f"*{side}*")

print(top)
for i in range(a - 2):
    print(sides)
print(top)