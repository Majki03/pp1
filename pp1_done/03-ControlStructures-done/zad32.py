interested = input("Are you interedsted in computer science (Y/N): ").upper()
playing = input("Do you like playing computer games (Y/N): ").upper()
ig = input("Do you have an Intagram account (Y/N): ").upper()

if(interested == "Y"):
    inte = "Yes"
else:
    inte = "No"
if(playing == "Y"):
    pl = "Yes"
else:
    pl = "No"
if(ig == "Y"):
    insta = "Yes"
else:
    insta = "No"

print("Interested in computer science:", inte)
print("Playing computer games:", pl)
print("Has an Instahram account:", insta)