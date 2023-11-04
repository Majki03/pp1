import random

results = random.randint(1, 6)

guess = input("Guess the number: ")

is_it = results == int(guess)

print("The number is:", results)
print("Your number:", guess)
print("Did you get it?", is_it)