import random

def rand_elem(array):
    return random.choice(array)

arr = ["Kasia", 1, 2, [5, 6, 8], 1.3, "Karolina"]

random_elem = rand_elem(arr)
print(random_elem)