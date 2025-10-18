def main():
    print("Program starting.")
    first_name, last_name, file_name = getUserInput()
    # Create the file and add user input:
    file = open(f"{file_name}", "w")
    file.write(first_name + "\n" + last_name + "\n")
    print("Program ending.")


def getUserInput():
    first_name = input("Insert first name: ")
    last_name = input("Insert last name: ")
    file_name = input("Insert filename: ")
    return first_name, last_name, file_name
main()