n = int(input("Enter N: "))

count, number = 0, 2
while count < n:
    if all(number % i for i in range(2, int(number**0.5) + 1)):
        print(number, end=" ")
        count += 1
    number += 1

print()