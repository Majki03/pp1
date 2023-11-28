number = input("Enter vehicle registration number: ")

if(number.startswith("KR") or number.startswith("KK")):
    print("Car from Kraków: True")
else:
    print("Car from Kraków: False")