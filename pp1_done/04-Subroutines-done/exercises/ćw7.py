def comutegrade(wart):
    if(wart <= 1.0 and wart >= 0.9):
        return 5.0
    elif(wart < 0.9 and wart >= 0.8):
        return 4.5
    elif(wart < 0.8 and wart >= 0.7):
        return 4.0
    elif(wart < 0.7 and wart >= 0.6):
        return 3.5
    elif(wart < 0.6 and wart >= 0.5):
        return 3.0
    elif(wart < 0.5 and wart >= 0.0):
        return 2.0

w = input("Podaj wartość (0.0 - 1.0): ")

try:
    f_w = float(w)
    print(comutegrade(f_w))
except:
    print("Niepoprawna wartość")