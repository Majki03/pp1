code = "0805"

for i in range(3):
    pin = input("Enter the PIN code: ")
    if(pin == code):
        break
    else:
        print("Invorrect...")
else:
    print("Sorry, your payment card has been blocked")