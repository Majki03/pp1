height = 183

h_feet = (183 / 2.54)
height_feet = h_feet / 12
height_inches = h_feet - height_feet * 12

print(f"I am {height}cm tall, i.e. {height_feet:.0f} feet and {height_inches:.0f} inches")