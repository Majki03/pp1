arr = ["Genowefa", "Onurfy", "Celestyna", "Alojzy", "Pankracy"]
print("Name:", " ".join(map(str, arr)))

longest = ""
for i in arr:
    if(len(i) > len(longest)):
        longest = i
print("Longest name:", longest)