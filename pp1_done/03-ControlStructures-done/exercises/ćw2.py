hours = input("Podaj liczbe godzin: ")
rate = input("Podaj stawkę godzinową: ")

try:
    if(hours <= 40):
        print(f"Wynagrodzenie: {hours * rate}")
    elif(hours > 40):
        print(f"Wynagrodzenie: {40 * rate + ((hours - 40) * (rate * 1.5))}")
except:
    print("Błąd, podaj wartość numeryczną")