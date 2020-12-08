import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")
    connection.commit()


def add_entry(entry_content, entry_date):
    connection.execute(
        "INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date)
        ) #this is done to prevent SQL injection
    connection.commit()

def get_entries():
   return entries
        

