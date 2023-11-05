price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

reduction = price * (discount / 100)
price_d = price - reduction

print(f"Price with discount: {price_d:.2f}")
print(f"Reduction: {reduction:.2f}")