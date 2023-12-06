#import matplotlib.pyplot as plt

#x = []
#y = []

# create x values
#for n in range(-100,101):
#    x = x + [n]

# create y values
#for n in x:
#    y = n**2 - 3

# display chart
#plt.plot(x, y, label = "f(x) = x^2 - 3")
#plt.xlabel("x")
#plt.ylabel("f(x)")
#plt.title("Graph of f(x) = x^2 - 3")
#plt.axhline(0, color = "black", linewidth = 0.5)
#plt.axvline(0, color = "black", linewidth = 0.5)
#plt.grid(color = "gray", linestyle = "--", linewidth = 0.5)
#plt.legend()
#plt.show()

import matplotlib.pyplot as plt

# Create x values
x = list(range(-100, 101))

# Create y values for f(x) = x^2 - 3 using list comprehension
y = [n**2 - 3 for n in x]

# Display chart
plt.plot(x, y, label='f(x) = x^2 - 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = x^2 - 3')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()