from stack import push, pop, empty, display

def decimal_to_binary(number):
    while number > 0:
        remainder = number % 2
        push(remainder)
        number //= 2

def display_binary_result():
    binary_result = ""
    while not empty():
        binary_result += str(pop())

    return binary_result

# Input natural number
natural_number = int(input("Enter a natural number: "))

# Convert the number to binary using a stack
decimal_to_binary(natural_number)

# Display the conversion steps
print("\nDivision\tRemainder")
while not empty():
    binary_digit = pop()
    print(f"{natural_number} / 2 = {natural_number // 2}\t{binary_digit}")
    natural_number //= 2

# Display the final result
print(f"\nNatural number: {natural_number}")
print(f"Binary number: {display_binary_result()}")