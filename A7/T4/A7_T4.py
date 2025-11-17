
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def readTimestamps(PFilename: str, timestamps) -> None:
    tempRows: list[str] = []
    print('Reading file "{}".'.format(PFilename))
    timestamps.clear()
    file = open(PFilename, "r")
    while True:
        line = file.readline()
        if line.startswith("Weekday") or line == '\n':
            continue
        #remove newline
        row = line.rstrip()
        if row != "":
            tempRows.append(row)
        if len(line) == 0:
            break
    file.close()
    #analyse timestamps
    tempList = []
    for weekday in WEEKDAYS:
        for row in tempRows:
            if row.startswith(weekday):
                listItem = row.split(";")
                tempList.append(listItem)
    timestamps.extend(tempList)
    # return tempList
    return None

def TIMESTAMP() -> None:
    print("Timestamp module.")
    return None


def displayTimestamps(results: list[list[str]]) -> None:
    print("Electricity usage:")
    for i in results :
        weekday = i[0]
        hour = i[1]
        price = i[3]
        consumption = f"{i[2]}.00"
        total = int(i[2]) * float(i[3])
        print(f" - {weekday} {hour}:00, price {price}, consumption {consumption} kWh, total {round(total, 2)}  €")
    return None

def main() -> None:
    print("Program starting.")
    timestamps: list[str] = []
    PResults: list[str] = []
    fileName = input("Insert filename: ")
    readTimestamps(fileName, timestamps)
    # results = analyseTimestamps(timestamps)
    displayTimestamps(timestamps)
    # print(results)
    timestamps = []
    PResults = []
    return None


if __name__ == "__main__":
    main()
