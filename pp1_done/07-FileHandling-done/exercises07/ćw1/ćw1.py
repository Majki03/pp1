name = input("Podaj nazwę pliku: ")

f = open(name)

for line in f:
    line = line.rstrip()
    print(line.upper())