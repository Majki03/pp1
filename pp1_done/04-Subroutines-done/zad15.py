def phone_keyboard():
  for i in range(6, -1, -3):
    for j in range(1, 4):
      print(f"{i + j} ", end = "")
    print()

phone_keyboard()