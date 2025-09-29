# A3_T5 Temperature converter (TEST TASK)
# Create a temperature unit conversion program.

# Start the program by listing options for the user:

# Celsius to Fahrenheit
# Fahrenheit to Celsius
# Exit
# Prompt user to insert choice. After the decision to convert, ask the amount of current temperature (use the floating point datatype). Lastly show the converted value to the user.

# For the unit conversions, use the formula Celsius = (Fahrenheit - 32) / 1.8

# Data representation examples:

# 50.0 °F
# 10.0 °C
# If the user chooses option Exit, notify the user: Exiting...

# Use 1 decimal precision to round the converted value.

# Example program runs

# run 1 run 2 run 3
print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
userSelection = input("Your choice: ")
if userSelection == "0":
    print("Exiting...")
elif userSelection == "1":
    celcius = float(input("Insert the amount of Celsius: "))
    fahrenheit = 9/5 * celcius + 32
    print(f"{celcius} °C equals to {round(fahrenheit, 1)} °F")
elif userSelection == "2":
    fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    celcius = 5/9 * (fahrenheit - 32)
    print(f"{fahrenheit} °F equals to {round(celcius, 1)} °C")
else:
    print("Unknown option.")


print("\nProgram ending.")