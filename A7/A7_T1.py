def main():
    print("Program starting.")
    print("Collect positive integers.")

    integers = [] 
    user_input = 0
    while (user_input >= 0):
        try:
            user_input = int(input("Insert positive integer (negative stops): "))
            if user_input <= 0:
                break
            else:
                integers.append(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("Stopped collecting positive integers.")

    if integers:
        print(f"Displaying {len(integers)} integers:")
        for index, value in enumerate(integers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")
    else:
        print("No integers to display.")

    print("Program ending.")


# Run the program
if __name__ == "__main__":
    main()
