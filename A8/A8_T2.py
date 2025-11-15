def askIntegers(values: list[int]) -> None:
    commaSepString = input("Insert comma separated integers: ")
    values.extend(commaSepString.split(","))
    return None

def analyze(values: list[int]):
    newValues: list[int] = []
    for value in values:
        try:
            intValue = int(value)
            newValues.append(intValue)
        except:
            print(f"Invalid value '{value}' detected.") 
    values.clear()
    values.extend(newValues)
    return None

def main():
    print("Program starting.")
    values: list[int] = []
    askIntegers(values)
    analyze(values)
    integerCount = len(values)
    integerSum = sum(values)
    if integerCount == 0:
        print("No values to analyse.")
    else:
        print(f"There are {integerCount} integers in the list.")
        print(f"Sum of the integers is {integerSum} and it's {"odd" if integerSum % 2 else "even"}")

    print("Program ending.")



if __name__ == "__main__":
    main()