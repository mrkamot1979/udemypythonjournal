entries = []

def addEntry():
    entrycontent = input("Please enter first data: ")
    entrydate = input("Enter date: ")
    entries.append({"entrycontent" : entrycontent, "entrydate" : entrydate})

def viewEntry():
    for entry in entries:
        print(f"{entry['entrycontent']}\n{entry['entrydate']}\n\n")
        
    

