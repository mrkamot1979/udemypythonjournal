from databaseclone import addEntry, viewEntry

welcomemsg = "Welcome to the Clone"

menumsg = """
Pick one Mofo
1. Add data
2. View data
3. Exit

Your selection : 
"""

print(welcomemsg)


while (userinput := input(menumsg))!= "3":
    if (userinput == "1"):
        addEntry()
    elif (userinput == "2"):
        viewEntry()
    else:
        print("Invalid input, please try again")





