def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

if __name__ == "__main__":
    # check if function works
    num = int(input("Enter digits: "))
    
    print(sum_digits(num))