
def analyseValues(content):
    count = 0
    sum = 0
    greatest = 0
    avg = 0.00
    for line in content:
        sum += int(line)
        count += 1
        if int(line) > greatest:
            greatest = int(line)
    avg = f"{sum / count:.2f}"
    dataset = f"Count;Sum;Greatest;Average\n{count};{sum};{greatest};{avg}\n"
    return dataset

def readValues(fileName):
    try:
        lines = []
        content = open(fileName, "r")
        for line in content:
            line = line.strip()
            lines.append(line)

        content.close()
        return lines
    except FileNotFoundError:
        content.close()
        print("File not found. Program ending.")
        return ""




def main():
    print("Program starting.")
    fileName = input("Insert filename: ")
    values = readValues(fileName)
    result = analyseValues(values)
    print("#### Number analysis - START ####")
    print(f"File \"{fileName}\" results:")
    print(result)
    print("#### Number analysis - END ####")
    print("Program ending.")

# main()
if __name__ == "__main__":
    main()
