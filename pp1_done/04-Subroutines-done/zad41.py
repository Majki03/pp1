def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(n):
    count = 0
    candidate = 1

    while count < n:
        candidate += 1
        if prime(candidate):
            count += 1

    return candidate

result1 = f(1)
result2 = f(5)

print(result1)
print(result2)