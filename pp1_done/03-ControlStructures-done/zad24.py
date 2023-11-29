price = float(input("Enter product price: "))
decrese = float(input("Enter how much it decreses: "))

reduced = (decrese / price) * 100
current = price - decrese

if(reduced >= 10):
    print(f"Current product price: {current:.1f}")
    print(f"Previous product price: {price:.1f}")
    print("Buy the product!")
    print(f"Product price reduced by {reduced:.0f}%")
else:
    print("Still nothing ;(")