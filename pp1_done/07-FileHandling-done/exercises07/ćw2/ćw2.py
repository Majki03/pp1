name = input("Podaj nazwę pliku: ")

try:
    count = 0
    sum = 0
    with open(name) as plik:
        for line in plik:
            line = line.rstrip()
            if(not line.startswith("X-DSPAM-Confidence:")):
                continue
            else:
                count += 1
                line_num = line.split()
                sum += float(line_num[1])
        av = sum / count
        print("Średni poziom pewności spamu", av)
except:
    print("Nie można odnaleźć pliku, sprawdź podaną nazwę")