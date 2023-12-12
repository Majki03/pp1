import re

name = input("Podaj nazwę pliku: ")

try:
    with open(name) as file:
        count = 0
        suma = 0
        for line in file:
            line = line.rstrip()
            x = re.findall("^New Revision: ([0-9]+)", line)
            if(not x):
                continue
            else:
                av = sum(map(int, x)) / len(x)
        print(int(av))
except:
    print("Nie poprawna nazwa pliku, sprawdź nazwę")