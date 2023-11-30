def comutepay(hours, rate):
    wynag = 40 * rate + ((hours - 40) * (rate * 1.5))
    return wynag

h = float(input("Podaj liczbę godzin: "))
r = float(input("Podaj stawkę godzinową: "))

if(h <= 40):
    print("Wynagrodzenie:", h * r)
elif(h > 40):
    print("Wynagrodzenie:", comutepay(h, r))