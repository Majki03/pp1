from stack import push, pop, empty, display

def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

def calculate_rpn(expression):
    for value in expression:
        if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
            push(float(value))
        elif value in ['+', '-', '*', '/']:
            operand2 = pop()
            operand1 = pop()
            result = perform_operation(value, operand1, operand2)
            push(result)
        elif value == '=':
            return pop()

# Examples of RPN expressions
expression1 = ['2', '3', '+', '=']
expression2 = ['2', '4', '1', '+', '*','=']
expression3 = ['2', '3', '+', '4', '5', '+', '*', '=']
expression4 = ['8', '3', '1', '+', '/', '3', '2', '-', '4', '+', '*','=']

# Calculate and display results
result1 = calculate_rpn(expression1)
print(f"Result 1: {result1}")

result2 = calculate_rpn(expression2)
print(f"Result 2: {result2}")

result3 = calculate_rpn(expression3)
print(f"Result 3: {result3}")

result4 = calculate_rpn(expression4)
print(f"Result 4: {result4}")