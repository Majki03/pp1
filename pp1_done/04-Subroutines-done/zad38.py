def f(palindrome):
    return palindrome == palindrome[::-1]

result1 = f("radar")
result2 = f("12-11-21")
result3 = f("book")

print(result1)
print(result2)
print(result3)