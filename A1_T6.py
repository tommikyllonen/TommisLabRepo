# Create a Python program that is able to calculate remainder. Remainder can be calculated using modulo “%” operator. See also “modulus” example in W3Schools.

#1. Prompt user “Insert an integer: ” and assign the input value into Feed variable
#2. Convert the Feed into an integer and assign it to Value variable
#3. Calculate the remainder of the Value when divided by 2 and assign it to the Remainder variable.
#4. Print the inserted value “Value is {Value}”
#5. Print the remainder value “The remainder is {Remainder} when {Value} is divided by 2.”
# Example program run:

# Insert an integer: 479
# Value is 479
# The remainder is 1 when 479 is divided by 2.

Feed = input("Insert an integer: ")
Value = int(Feed)
Remainder = Value % 2
print(f"Value is {Value}")
print(f"The remainder is {Remainder} when {Value} is divided by 2.")
