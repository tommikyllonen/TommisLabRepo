def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    inputFileName = input("Insert filename to read: ")
    print(f"Reading names from \"{inputFileName}\".")
    names = getNames(inputFileName)
    if len(names) == 0: 
        return
    shortestName = len(names[0])
    longestName = 0
    namesCombined = ""
    nameCount = len(names)



    for name in names:
        namesCombined += name
        if (len(name) < shortestName and len(name) != 0):
            shortestName = len(name)
        if (len(name) > longestName):
            longestName = len(name)
    print("Analysing names...")
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print(f"Name count - {nameCount}")
    print(f"Shortest name - {shortestName} chars")
    print(f"Longest name - {longestName} chars")
    print(f"Average name - {(len(namesCombined)/nameCount):.2f} chars")
    print("#### REPORT END ####")
    print("Program ending.")
    print("")

def getNames(inputFileName):
    names = []
    try:
        content = open(inputFileName, "r")
        while True:
            line = content.readline()
            if len(line.strip()) == 0:
                #if empty line, check if this was last line or just and empty line
                line = content.readline()
                if len(line.strip()) == 0:
                    break
                else:
                    names.append(line.strip())
                    continue
            names.append(line.strip())
        content.close()
        return names
    except FileNotFoundError:
        print(f"File \"{inputFileName}\" no names found. Exiting...")
        return []
    
main()