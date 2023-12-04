def f(amount_to_pay):
    count_5 = amount_to_pay // 5
    amount_to_pay %= 5

    count_2 = amount_to_pay // 2
    amount_to_pay %= 2

    count_1 = amount_to_pay

    sum = count_5 + count_2 + count_1

    return sum

amount = int(input("Enter amount to pay: "))

if __name__ == "__main__":
    print(f(amount))