hours = float(input("Podaj liczbe godzin: "))
rate = float(input("Podaj stawkę godzinową: "))

if(hours <= 40):
    print(f"Wynagrodzenie: {hours * rate}")
elif(hours > 40):
    print(f"Wynagrodzenie: {40 * rate + ((hours - 40) * (rate * 1.5))}")