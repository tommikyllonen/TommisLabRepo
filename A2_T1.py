# Make a Python program, which prompts the user name and two floating numbers. Multiply the inserted numbers to get product. Round the product in two decimal precision. Complete the program output as shown below.

# Example program run:

# Program starting.
# What is your name: John
# Enter a floating point number: 3.1
# Enter second floating point number: 5.3
# John you gave numbers 3.1 and 5.3
# Multiplying first and second number will result in product 16.43
# Program ending.

print("Program starting.")

name = input("What is your name: ")
float1 = float(input("Enter a floating point number: "))
float2 = float(input("Enter second floating point number: "))

print(f"{name} you gave numbers {float1} and {float2}")
print(f"Multiplying first and second number will result in product {float1 * float2}")
print("Program ending.")
