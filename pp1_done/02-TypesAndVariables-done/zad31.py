import random

roll = random.randint(1, 6)

guess = int(input("Enter what number had been rolled (1, 6): "))

if(roll == guess):
    print("True")
else:
    print("False")