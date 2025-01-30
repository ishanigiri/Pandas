import sqlite3
import requests
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

db_name = "orders.db"

def create_database():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY,
                        product TEXT NOT NULL,
                        quantity INTEGER NOT NULL,
                        price REAL NOT NULL,
                        customer_email TEXT NOT NULL
                    )''')
    connection.commit()
    connection.close()

def fetch_product_details(product_id):
    url = f"https://fakestoreapi.com/products/{product_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["title"], data["price"]
    else:
        return None, None

def store_order(product_id, quantity, customer_email):
    product_name, price = fetch_product_details(product_id)
    if product_name is None:
        print("Failed to fetch product details.")
        return
    total_price = price * quantity
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO orders (product, quantity, price, customer_email) VALUES (?, ?, ?, ?)",
                   (product_name, quantity, total_price, customer_email))
    connection.commit()
    connection.close()
    print(f"Order for {product_name} stored successfully.")

def generate_csv():
    connection = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT product, quantity, price, customer_email FROM orders", connection)
    connection.close()
    df.to_csv("order_summary.csv", index=False)
    print("Order summary saved as order_summary.csv")

def send_email(to_email, subject, message):
    EMAIL_ADDRESS = "ishanigiri7@gmail.com"  # Replace with actual email
    EMAIL_PASSWORD = "bprv yrks wseb oskh"   # Use an app password for security
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            email_message = MIMEMultipart()
            email_message['From'] = EMAIL_ADDRESS
            email_message['To'] = to_email
            email_message['Subject'] = subject
            email_message.attach(MIMEText(message, 'plain'))
            server.send_message(email_message)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def process_order(product_id, quantity, customer_email):
    store_order(product_id, quantity, customer_email)
    generate_csv()
    subject = "Order Confirmation"
    message = f"Thank you for your order! You purchased {quantity} unit(s) of product ID {product_id}."
    send_email(customer_email, subject, message)

if __name__ == "__main__":
    create_database()
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))
    customer_email = input("Enter customer email: ")
    process_order(product_id, quantity, customer_email)
