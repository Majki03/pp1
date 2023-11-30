def diffrent(n1, n2, n3):
  if(n1 != n2 and n1 != n3 and n2 != n3):
    return True
    
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

if(diffrent(first, second, third)):
  print(f"Numbers {first}, {second} and {third} are diffrent")