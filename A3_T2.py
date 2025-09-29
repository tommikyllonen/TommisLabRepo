# A3_T2 String comparisons
# Make Python program which does the following steps:

# Prompt user to insert
# A word
# A character
# Find if the character exists in the word. Possible prints below.
# Word "{WordFirst}" contains character "{Character}"
# Word "{WordFirst}" doesn't contain character "{Character}"
# Prompt user to insert one more word
# Compare the first word to the second word. Examples below:
# The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
# The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
# Both inserted words are the same alphabetically, "{WordFirst}"
# Example program run

# run 1
# Program starting.
# String comparisons
# Insert first word: beans
# Insert a character: n
# Word "beans" contains character "n"
# Insert second word: banana
# The second word "banana" is before the first word "beans" alphabetically.
# Program ending.


print("Program starting.")
print("String comparisons")
firstWord = input("Insert first word: ")
character = input("Insert a character: ")
includes = character in firstWord
if(includes):
    print(f'Word "{firstWord}" contains character "{character}"')
else:
    print(f'Word "{firstWord}" doesn\'t contain character "{character}"')
secondWord = input("Insert second word: ")
if secondWord == firstWord:
    print(f'Both inserted words are the same alphabetically, "{firstWord}"')
elif secondWord  < firstWord:
    print(f'The second word "{secondWord}" is before the first word "{firstWord}" alphabetically.')
else:
    print(f'The first word "{firstWord}" is before the second word "{secondWord}" alphabetically.')
print("Program ending.")
