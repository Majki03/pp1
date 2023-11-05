import random

resulds = random.randint(1, 6)

special = resulds == 1 or resulds == 6

print("Dice rolles", resulds)
print("Special number", special)