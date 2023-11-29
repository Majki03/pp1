age = int(input("Enter the dog's age in human years: "))
                
mniej_2 = age * 10.5
wiecej_2 = 2 * 10.5 + (age - 2) * 4

if(age <= 2):
    print(f"The dog's age in dog’s years is {mniej_2:.1f} years.")
else:
    print(f"The dog's age in dog’s years is {wiecej_2:.1f} years.")