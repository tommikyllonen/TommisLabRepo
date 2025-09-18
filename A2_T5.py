# A2_T5 String length and slicing (TEST TASK)
# Make a Python program, which prompts for a compound word.

# Get following aspects from the word
# Length
# First character
# Reversed version e.g. “Suitcase” is reversed “esactiuS”
# Display the aspects using print commands.
# Prompt the user to take substring from the existing compound word.
# Finally print the user specified substring.
# Example program run:

# Program starting.

# Insert a closed compound word: Moonbanana
# The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
# The inserted word length is 10
# Last character is 'a'

# Take substring from the inserted word by inserting...
# 1) Starting point: 0
# 2) Ending point: 4
# 3) Step size: 1

# The word 'Moonbanana' sliced to the defined substring is 'Moon'.
# Program ending.

##START HERE######################################

print("Program starting.")

compoundWord = input("Insert a closed compound word: ")
reverseWord = compoundWord[::-1]
wordLen = len(compoundWord)
print(f"The word you inserted is '{compoundWord}' and in reverse it is '{reverseWord}'.")
print(f"The inserted word length is {wordLen}")
print(f"Last character is '{compoundWord[wordLen - 1]}'") 
print("Take substring from the inserted word by inserting...")
startingPoint = int(input("1) Starting point: "))
endingPoint = int(input(f" 2) Ending point: "))
steps = int(input(f"3) Step size: "))

substring = compoundWord[startingPoint:endingPoint:steps]###FIX ME FIX FIX ME FIX FIX ME FIX FIX ME FIX 
print(f"The word '{compoundWord}' sliced to the defined substring is '{substring}'.")
print("Program ending.")