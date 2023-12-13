with open("MeatAndFish.txt") as file1:
  maf = file1.read()

with open("GrainsAndBread.txt") as file2:
  gab = file2.read()

with open("allproducts.txt", "w") as copy:
  copy.write(maf)
  copy.write("\n")
  copy.write(gab)