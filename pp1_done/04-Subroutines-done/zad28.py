def f(binary_number):
    for i in binary_number:
        if(i not in {"0", "1"}):
            return False
    return True

binary = str(input("Enter binary number: "))
        
if __name__ == "__main__":
    print(f(binary))