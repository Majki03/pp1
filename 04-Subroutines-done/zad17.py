def diffrent(n1, n2, n3):
    return n1 != n2 and n1!= n3 and n2 != n3

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if(diffrent(n1, n2, n3)):
    print(f"Numbers {n1}, {n2} and {n3} are diffrent.")
else:
    print(f"The numbers are not all different.")