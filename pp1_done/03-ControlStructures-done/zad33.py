dec = int(input("Enter decimal number: "))

quotionten = dec
binary = ""

while quotionten > 0:
  remainder = quotionten % 2
  binary = str(remainder) + binary
  quotionten = quotionten // 2
  
print(f"{dec}(10) = {binary}(2)")