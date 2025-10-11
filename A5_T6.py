def main():
    userSelection = -1
    count = 0
    print("Program starting.")
    while True:
        showOptions()
        userSelection = askChoice()
        if userSelection == 0:
            print("Exiting program...")
            break
        if userSelection == 1:
            print(f"Current count - {count}")
        if userSelection == 2:
            count += 1
            print("Count increased!")
        if userSelection == 3:
            count = 0
            print("Cleared count!")
        if userSelection == -1 or userSelection not in range(4):
            print("Unknown option!")
        print("")
    print("\nProgram ending.")
        
def askChoice() -> int:
        userSelection = input("Your choice: ")
        if not userSelection.isnumeric():
            return -1
        return int(userSelection)

def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

main()