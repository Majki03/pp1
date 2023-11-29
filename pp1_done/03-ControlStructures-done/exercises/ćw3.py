number = input("Podaj wartość pomiędzy 0.0 a 1.0: ")

try:
    wart = float(number)

    if(wart <= 1.0 and wart >= 0.9):
        print("5.0")
    elif(wart < 0.9 and wart >= 0.8):
        print("4.5")
    elif(wart < 0.8 and wart >= 0.7):
        print("4.0")
    elif(wart < 0.7 and wart >= 0.6):
        print("3.5")
    elif(wart < 0.6 and wart >= 0.5):
        print("3.0")
    elif(wart < 0.5 and wart >= 0.0):
        print("2.0")
except:
    print("Niepoprawna wartość")