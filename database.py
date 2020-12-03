entries = []

def add_entry(entry_content, entry_date):
    entries.append({"content" : entry_content, "date" : entry_date})

def view_entry():
    for entry in entries:
        print(f"{entry['content']}\n{entry['date']}\n\n")
        

