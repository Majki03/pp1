name = input("Podaj nazwę pliku: ")

try:
    with open(name) as file:
        count = 0
        for line in file:
            line = line.rstrip()
            if(not line.startswith("Subject:")):
                continue
            else:
                count += 1
        print(f"Mamy {count} linii z tematem wiadomości w pliku {name}")
except:
    if(name.lower() == "trele morele"):
        print("TRELE MORELE - co za bzdury!")
    else:
        print("Nie można otworzyć pliku:", name)