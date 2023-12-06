import numpy as np
import matplotlib.pyplot as plt

# Generate x values in degrees from 0 to 360
x_degrees = np.arange(0, 361, 1)

# Convert degrees to radians for the sine function
x_radians = np.radians(x_degrees)

# Calculate y values for y = sin(x)
y = np.sin(x_radians)

# Plot the graph
plt.plot(x_degrees, y, label='y = sin(x)')
plt.xlabel('Angle (degrees)')
plt.ylabel('y')
plt.title('Graph of y = sin(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()