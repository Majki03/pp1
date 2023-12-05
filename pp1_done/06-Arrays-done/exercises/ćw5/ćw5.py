fhand = open("mbox-short.txt")

count = 0

for line in fhand:
    words = line.split()
    #print("Debug:", words)
    if(len(words) == 0 or words[0] != "From"): continue
    if(words[0] == "From"):
        count += 1
    print(words[1])

print(f"Mamy {count} linii, w których From jest pierwszym wyrazem")