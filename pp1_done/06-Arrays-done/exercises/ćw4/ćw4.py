slowa = []

with open("romeo.txt", "r") as plik:
    for linia in plik:
        s_linii = linia.split()

        for slowo in s_linii:
            slowo = slowo.strip(".,!?()[]{}\'")

            if slowo not in slowa:
                slowa.append(slowo)

slowa.sort()
print(slowa)