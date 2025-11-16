def main():
    print("Program starting.")
    print("Collect positive integers.")
    positiveIntegers = []
    userInput = 1
    while(userInput > 0):
            userInput = int(input("Insert positive integer(negative stops): "))
            if (userInput > 0):
                positiveIntegers.append(userInput)
            else: 
                break
    print("Stopped collecting positive integers.")
    if (len(positiveIntegers) == 0):
         print("No integers to display.")
    else:
        print(f"Displaying {len(positiveIntegers)} integers:")
        for i in range(len(positiveIntegers)):
             print(f"- Index {i} => Ordinal {i + 1} => Integer {positiveIntegers[i]}")
    print("program ending")



if __name__ == "__main__":
    main()
    
