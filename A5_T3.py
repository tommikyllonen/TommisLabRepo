def main():
    print("Program starting.")
    userName = askName()
    greetUser(userName)
    print("Program ending.")

def askName():
    name = input("Insert name: ")
    return name

def greetUser(name):
    print (f"Hello {name}!")
