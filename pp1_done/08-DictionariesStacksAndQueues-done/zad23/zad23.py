from stack import push, pop, empty, display

# Display stack
print("a. Display stack:")
display()

# Put numbers on the stack
print("\nb. Put the number 2 on the stack:")
push(2)

print("c. Put the number 14 on the stack:")
push(14)

print("d. Put the number 9 on the stack:")
push(9)

# Display stack
print("\ne. Display stack:")
display()

# Get element from stack
print("\nf. Get element from stack:")
element = pop()
if element is not None:
    print(f"Element retrieved: {element}")
else:
    print("Stack is empty.")

# Display stack
print("\ng. Display stack:")
display()

# Put numbers on the stack
print("\nh. Put the number 31 on the stack:")
push(31)

print("i. Put the number 6 on the stack:")
push(6)

# Display stack
print("\nj. Display stack:")
display()

# Get two elements from stack
print("\nk. Get two elements from stack:")
element1 = pop()
element2 = pop()

if element1 is not None and element2 is not None:
    print(f"Elements retrieved: {element1}, {element2}")
else:
    print("Not enough elements in the stack.")

# Display stack
print("\nl. Display stack:")
display()