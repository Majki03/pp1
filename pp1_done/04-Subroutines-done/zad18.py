def numbers(n):
  num_list = [str(i) for i in range(1, n + 1)]
  return " ".join(num_list)
    
  
num_15 = numbers(15)
num_7 = numbers(7)

print("Numbers <1, 15>:", num_15)
print("Numbers <1, 7>:", num_7)