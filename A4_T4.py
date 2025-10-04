print("program starting.")
print("")

userword = " "
wordcount = 0
charcount = 0

while userword != "": 
    userword = input("insert word (empty stops): ")
    if(len(userword) != 0 and userword != " " and userword != "" ):
        wordcount +=  1
        charcount += len(userword)
print("")
print("you inserted:")
print(f"- {wordcount} words")
print(f"- {charcount} characters")
print("")
print("Program ending.")