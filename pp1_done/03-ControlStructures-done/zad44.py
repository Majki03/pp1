sum = 0
quan = 0

while True:
    num = int(input("Enter number: "))
    if(num == 0):
        break
    sum += num
    quan += 1

mean = sum / quan if quan > 0 else 0

print(f"Results: Quantity={quan}, Sum={sum}, Mean={mean}")