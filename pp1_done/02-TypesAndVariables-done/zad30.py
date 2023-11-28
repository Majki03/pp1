import random

roll = random.randint(1, 6)

if(roll == 1 or roll == 6):
    print("Dice rolled:", roll)
    print("Special number: True")
else:
    print("Dice rolled:", roll)
    print("Special number: False")