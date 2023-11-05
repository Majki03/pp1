def numbers(n):
    num_list = [str(i) for i in range(1, n + 1)]
    return " ".join(num_list)

result_15 = numbers(15)
result_7 = numbers(7)

print("Numbers <1, 15>:", result_15)
print("Numbers <1, 7>:", result_7)