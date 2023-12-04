def f(name):
    words = name.split()
    return ''.join(word[0] for word in words)

result1 = f("Internet of Things")
result2 = f("For Your Information")
result3 = f("Python")

print(result1)
print(result2)
print(result3)