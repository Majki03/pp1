def read_number():
  num = int(input("Enter a number: "))
  return num
  
if __name__ == "__main__":
  num1 = read_number()
  num2 = read_number()
  suma = num1 + num2
  
  print(f"{num1} + {num2} = {suma}")