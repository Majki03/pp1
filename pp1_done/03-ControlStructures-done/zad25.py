amount = int(input("Number of products purchased: "))
price = float(input("Product price: "))

pay = price * amount
pay_d = (2 * price) + (amount - 2) * (price * 0.75)

if(amount > 2):
    print(f"Amount to pay: {pay_d:.2f}")
else:
    print(f"Amount to pay: {pay:.2f}")