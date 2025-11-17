
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def readTimestamps(PFilename: str, timestamps, dailyUsage) -> None:
    tempRows: list[str] = []
    print('Reading file "{}".'.format(PFilename))
    dailyUsage.clear()
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
    tempDailyList = []
    for weekday in WEEKDAYS:
        weekday = weekday
        consumption = 0
        price = 0
        for row in tempRows:
            if row.startswith(weekday):
                listItem = row.split(";")
                # add items to total
                consumption += float(listItem[2])
                price += float(listItem[2]) * float(listItem[3])
                tempList.append(listItem)
        tempDailyList.append([weekday, consumption, price])
    dailyUsage.extend(tempDailyList)
    timestamps.extend(tempList)
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


def displayAverages(dailyUsage) -> None:
    print("Analysing timestamps.")  
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for day in dailyUsage:
        weekday = day[0]
        usage = f"{day[1]:.2f}"
        cost = f"{day[2]:.2f}"
        print(f" - {weekday} usage {usage} kWh, cost {cost} €")
    print("### Electricity consumption summary ###")

def main() -> None:
    print("Program starting.")
    dailyUsage = []
    timestamps: list[str] = []
    PResults: list[str] = []
    fileName = input("Insert filename: ")
    readTimestamps(fileName, timestamps, dailyUsage)
    # displayTimestamps(timestamps)
    displayAverages(dailyUsage)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()

