
def main():
    print("Program starting.")
    print("This program can read a file.")
    fileName = input("Insert filename: ")
    print(f"#### START \"{fileName}\" ####")
    file = open(fileName, "r")
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        print(line.strip())

    print(f"\n#### END \"{fileName}\" ####")
    print("Program ending.")


main()