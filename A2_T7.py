# A2_T7 Fahrenheit to Celcius
# Create a Python program to convert Fahrenheit to Celcius. Round the Celsius to 1 decimal precision.

# Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8

# Example program run:

print("Program starting.")

Fahrenheit = int(input("Insert fahrenheits: "))
Celcius = (Fahrenheit - 32) / 1.8
print(f" {Fahrenheit}°F is {round(Celcius,2)}°C")

print("Program ending.")