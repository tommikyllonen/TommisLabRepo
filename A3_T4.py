

# Extend the previous menu program by adding three more options to the menu.

# Options:

# Print the name backwards
# Your name backwards is "{NameBackwards}"
# Print the first character
# The first character in name "{Name}" is "{FirstChar}"
# Show the amount of characters in the name
# There are {NameLength} characters in the name "{Name}"


print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")
nameBackwards = name[::-1]
firstChar = name[0]
nameLength = len(name)
print("\nOptions")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")


response = input("Your choice: ")
if response == "1":
    print(f"Welcome {name}!")
elif response == "2":
    print(f"Your name backwards is \"{nameBackwards}\"")
elif response == "3":
    print(f'The first character in name "{name}" is "{firstChar}"')
elif response == "4":
    print(f'There are {nameLength} characters in the name "{name}"')
elif response == "0":
    print("Exiting...")
else:
    print("Unknown option.")
    
print("\nProgram ending.")