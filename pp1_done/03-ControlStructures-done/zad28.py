ean = input("Enter EAN-13 article number: ")

l_ean = len(ean)
s_ean = ean.startswith("590")

try:
    if(int(l_ean) == 13 and s_ean):
        print("Article number is correct")
        print("Article manufactured in Poland")
    elif(int(l_ean) == 13):
        print("Article number is correct")
    elif(int(ean)):
        print("Article number isn't correct")
except:
    print("Invalid value, pleas enter numbers")