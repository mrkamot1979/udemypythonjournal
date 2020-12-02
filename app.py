menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

your selection : """

welcome = "Welcome to the programming diary!"

print(welcome)

while (user_input := input(menu))!= "3": #walrus feature available in 3.8, essentially it becomes a BOOLEAN
    if (user_input == "1"):
        print("Adding")
    elif (user_input == "2"):
        print("Viewing Entries")
    else:
        print("Invalid option, please try again")




        




