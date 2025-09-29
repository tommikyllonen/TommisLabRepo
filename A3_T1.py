# A3_T1 If-statements
# Make Python program and implement if-statements in proper places.

# Ask user to insert two integers
# Compare the integers and then announce the greater number
# Create sum of the two intege0jjs
# Check the parity of the sum (see modulo-operator ‘%’)
# Other possible output variants:

# Integer comparison
# Integers are the same.
# First integer is greater.
# Parity check # Sum is even.  # Example program run
# Program starting.
# Insert two integers.
# Insert first integer: 5
# Insert second integer: 5
# Comparing inserted integers.
# Integers are the same

# Adding integers together
# 5 + 5 = 10

# Checking the parity of the sum...
# Sum is even.
# Program ending.
 


print("Program starting.")
print("Insert two integers.")
int1 = int(input("Insert first integer: "))
int2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")
aresame = int1 == int2
result = ""
if aresame:
    result = "Integers are the same"
elif int1 < int2:
    result = "Second integer is greater."
else:
    result = "first integer is greater"
print(result)

thesum = int1 + int2

print("\nAdding integers together") 
print(f"{int1} + {int2} = {thesum}")


print("\nChecking the parity of the sum...")
if(thesum % 2 != 0):
    print("Sum is odd.")
else:
    print("Sum is even")
    # print(thesum % 2)

print("Program ending.")
