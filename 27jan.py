#using SQLite to interact with a database
import sqlite3
connection = sqlite3.connect("store.db")
cursor = connection.cursor()
#cretae a table for products
cursor.execute("""CREATE TABLE IF NOT EXISTS products (
    id INTEGER PIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
)""")
#insert data
cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("Laptop", 999.99))
connection.commit()
#Fetch data
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)
connection.close()
