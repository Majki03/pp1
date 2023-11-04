credit = input("Enter credit card number: ")

if(len(credit) == 16):
    print(f"Card number: {credit[:4]} {credit[4:8]} {credit[8:12]} {credit[12:]}")