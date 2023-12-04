num = int(input("Enter number: "))

def check(x, y):
    if(num >= x and num <= y):
        return bool(num)
    elif(num <= x and num >= y ):
        return bool(num)
    else:
        return False

if __name__ == "__main__":
    answer = check()