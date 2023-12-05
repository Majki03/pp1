numlist = list()
while True:
    inp = input("Wprowadź liczbę: ")
    if inp == "gotowe": break
    value = float(inp)
    numlist.append(value)

maxy = max(numlist)
mini = min(numlist)

print ("Największa:", maxy)
print ("Najmniejsza:", mini)
