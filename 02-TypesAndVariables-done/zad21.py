height = 183

inches = height / 2.54
feet = int(inches // 12)
remaining = int(inches % 12)

print(f"I am {height}cm tall, i.e. {feet} feet and {remaining} inches.")