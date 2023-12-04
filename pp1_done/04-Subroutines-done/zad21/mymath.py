import random

def generate_number():
    number = random.randint(1, 9)
    return number

if __name__ == "__main__":
    num = generate_number()