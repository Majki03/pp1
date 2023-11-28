celsius = int(input("Enter temperature in Celcius: ")) #user is entering the temperature in Celcius from keyboard

fahrenheit = celsius * 1.8 + 32 #program calculate temperature to Fahrenheits
kelvin = celsius + 273.15 #program calculate temperature to Kelvins

print(f"{fahrenheit:.2f}") #program display the results in Fahrenheits
print(f"{kelvin:.2f}") #program display the results in Kelvins