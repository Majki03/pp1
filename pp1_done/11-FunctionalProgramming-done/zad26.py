import matplotlib.pyplot as plt

temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

cities, temps = zip(*temperatures.items())

plt.bar(cities, temps, color='blue')
plt.title('Temperatures in Various Polish Cities')
plt.xlabel('Cities')
plt.ylabel('Temperature (°C)')

plt.show()