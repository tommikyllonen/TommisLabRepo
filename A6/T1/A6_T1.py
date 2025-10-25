
def main():
    print("Program starting.")
    print("This program can read a file.")
    fileName = input("Insert filename: ")
    file = open(fileName, "r")
    print(f"#### START \"{fileName}\" ####")
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        print(line.strip())

    print(f"\n#### END \"{fileName}\" ####")
    print("Program ending.")


main()