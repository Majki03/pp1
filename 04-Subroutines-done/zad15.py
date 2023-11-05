def phone_keyboard():
    for row in range(1, 10, 3):
        for number in range(row, row + 3):
            print(number, end=" ")
        print()

phone_keyboard()