price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

reduction = price * (discount / 100)
p_w_d = price - reduction

print(f"Price with discount: {p_w_d:.2f}")
print(f"Reduction: {reduction:.2f}")