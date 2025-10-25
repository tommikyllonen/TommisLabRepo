def main():
    print("Program starting.")
    print("This program can copy a file.")
    sourceFileName = input("Insert source filename: ")
    outputFileName = input("Insert destination filename: ")
    copyFile(sourceFileName, outputFileName)
    print("Program ending.")

def copyFile(sourceFileName, outputFileName):
    try:
        print(f"Reading file '{sourceFileName}' content.")
        sourceFile = open(sourceFileName, "r")
        outputFile = open(outputFileName, "w")
        content = sourceFile.read()
        outputFile.write(content)
        outputFile.close()
        sourceFile.close()
        print("File content ready in memory.")
        print(f"Writing content into file '{outputFileName}'.")
        print("Copying operation complete.")
    except FileNotFoundError:
        print(f"Source file '{sourceFileName}' not found. Exiting...")


main()    
    