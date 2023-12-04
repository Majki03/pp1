card_number = int(input("Enter card number: "))

def f(card_number):
    if(len(str(card_number)) == 16):
        for i in range(1):
            i = "*" * 10
        return i
    
if __name__ == "__main__":
    number = f()