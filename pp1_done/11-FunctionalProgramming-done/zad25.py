temp = {"Krakow":7, "Warszawa":-2, "Sopot":4, "Koszalin":-1, "Opole":3}

posi = list(filter(lambda x: temp[x] > 0, temp))

print("Cities with positive temperatures:", " ".join(posi))