userChoice = ""
while userChoice != "0":
    print("Program starting.")
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    userChoice = input("Your choice: ")
    if userChoice == "0":
        print("Exiting program...")
    elif userChoice == "1":
        userWord = input("Insert word: ")
    elif userChoice == "2":
        print(f"Current word - {userWord}")
    elif userChoice == "3":
        print(f'Word reversed - "{userWord[::-1]}"')
    else:
        print("Unknown option! try again.")
    print("")
