buys = float(input("Bank buys EUR: "))
sells = float(input("Bank sells EUR: "))

spread = sells - buys

print(f"Bank buys EUR: {buys:.4f}")
print(f"Bank sells EUR: {sells:.4f}")
print(f"Spread: {spread:.4f}")