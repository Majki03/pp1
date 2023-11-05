import mykeyboard

if __name__ == "__main__":
    num1 = mykeyboard.read_number()
    num2 = mykeyboard.read_number()

    total = num1 + num2
    print(f"{num1} + {num2} = {total}")