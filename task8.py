# Task: Design a simple to-do list with an SQL database.
# - Create a table for tasks (ID, description, due date).
# - Allow users to add, remove, and view tasks.

import sqlite3
import datetime

def user_input():
    todo = input("Enter todo: ")
    print("For Due date:")
    year = int(input("Enter year:"))
    month = int(input("Enter month:"))
    day = int(input("Enter day:"))
    due_date = datetime.date(year,month,day)
    return todo, due_date

def create_table():
    # Create a table schema for todo
    cursor.execute('''CREATE TABLE IF NOT EXISTS todo(
        id INTEGER PRIMARY KEY,
        description TEXT NOT NULL,
        due_date DATE NOT NULL
    )''')
def add_todo(todo, due_date):
    cursor.execute("INSERT INTO todo(description, due_date) VALUES (?, ?)", (todo, due_date))
    connection.commit()
    
def display_todo():
    # Fetch data from db
    cursor.execute("SELECT * FROM todo")
    for row in cursor.fetchall():
        print(row)
    
def remove_todo():
    del_todo = input("Enter todo you wish to remove: ")
    cursor.execute(f"DELETE FROM todo WHERE description='{del_todo}'")
    connection.commit()
    display_todo()

connection = sqlite3.connect("todo.db")
cursor = connection.cursor()
create_table()
while True:
    choice = input("Add todo?: y/n: ").lower()
    if choice != 'y':
        break
    todo, due_date = user_input()
    add_todo(todo=todo, due_date=due_date)
    
display_todo()
remove_todo()
