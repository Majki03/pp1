import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))
circumference = a + b + c

print(f"Triangle area: {area:.2f}")
print(f"Triangle circumferance: {circumference:.2f}")