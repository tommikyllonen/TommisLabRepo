WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def readFile(PFilename: str, PRows: list[str]) -> None:
    tempRows: list[str] = []
    print('Reading file "{}".'.format(PFilename))
    PRows.clear()
    file = open(PFilename, "r")
    while True:
        line = file.readline()
        if line.startswith("Weekday") or line == '\n':
            continue
        #remove newline
        row = line.rstrip()
        tempRows.append(row)
        # print(row)
        if len(line) == 0:
            break
    PRows.extend(tempRows)
    file.close()
    return None



def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    for weekday in WEEKDAYS:
        count = 0
        for row in PRows:
            if row.startswith(weekday):
                count += 1
        result = count
        PResults.append(result)
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for i in range(len(WEEKDAYS)):
        print(f"{WEEKDAYS[i]} {PResults[i]} stamps")
    print("### Timestamp analysis ###")
    return None

def main() -> None:
    print("Program starting.")
    PRows: list[str] = []
    PResults: list[str] = []
    fileName = input("Insert filename: ")
    readFile(fileName, PRows)
    analyseTimestamps(PRows, PResults)
    displayResults(PResults)
    PRows = []
    PResults = []
    return None


if __name__ == "__main__":
    main()
