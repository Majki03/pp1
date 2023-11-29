product = input("Washing product (jacket/underwear/shoes): ").lower()
rinse = input("Rinse (True/False): ").lower()
spin = input("Spin (True/False): ").lower()

count = 0

for i in range(1):
    if(product == "jacket"):
        count += 40
    else:
        count = count
    if(product == "underwear"):
        count += 70
    else:
        count = count
    if(product == "shoes"):
        count += 20
    else:
        count = count
    if(rinse == "true"):
        count += 15
    else:
        count = count
    if(spin == "true"):
        count += 9
    else:
        count = count

if(count == 64):
    print(f"Washing product = '{product}'")
    print("rinse =", rinse)
    print("spin =", spin)
    print(f"Total wasching time: {count} minutes")
elif(count == 55):
    print(f"Washing product = '{product}'")
    print("rinse =", rinse)
    print("spin =", spin)
    print(f"Total wasching time: {count} minutes")
elif(count == 49):
    print(f"Washing product = '{product}'")
    print("rinse =", rinse)
    print("spin =", spin)
    print(f"Total wasching time: {count} minutes")
elif(count == 40):
    print(f"Washing product = '{product}'")
    print("rinse =", rinse)
    print("spin =", spin)
    print(f"Total wasching time: {count} minutes")
elif(count == 94):
    print(f"Washing product = '{product}'")
    print("rinse =", rinse)
    print("spin =", spin)
    print(f"Total wasching time: {count} minutes")
elif(count == 85):
    print(f"Washing product = '{product}'")
    print("rinse =", rinse)
    print("spin =", spin)
    print(f"Total wasching time: {count} minutes")
elif(count == 79):
    print(f"Washing product = '{product}'")
    print("rinse =", rinse)
    print("spin =", spin)
    print(f"Total wasching time: {count} minutes")
elif(count == 70):
    print(f"Washing product = '{product}'")
    print("rinse =", rinse)
    print("spin =", spin)
    print(f"Total wasching time: {count} minutes")
elif(count == 44):
    print(f"Washing product = '{product}'")
    print("rinse =", rinse)
    print("spin =", spin)
    print(f"Total wasching time: {count} minutes")
elif(count == 35):
    print(f"Washing product = '{product}'")
    print("rinse =", rinse)
    print("spin =", spin)
    print(f"Total wasching time: {count} minutes")
elif(count == 29):
    print(f"Washing product = '{product}'")
    print("rinse =", rinse)
    print("spin =", spin)
    print(f"Total wasching time: {count} minutes")
elif(count == 20):
    print(f"Washing product = '{product}'")
    print("rinse =", rinse)
    print("spin =", spin)
    print(f"Total wasching time: {count} minutes")