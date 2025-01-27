import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import schedule
import time

# Email configuration
EMAIL_ADDRESS = "ishanigiri7@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "bprv yrks wseb oskh"      # Replace with your email password
SMTP_SERVER = "smtp.gmail.com"          # Replace with your email provider's SMTP server
SMTP_PORT = 587                          # Replace with your email provider's port

# Load tasks from CSV file
def load_tasks(csv_file):
    tasks = []
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['due_date'] = datetime.strptime(row['due_date'], "%Y-%m-%d")  # Parse due_date
                tasks.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return tasks

# Send an email reminder
def send_email(to_email, subject, message):
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
            print(f"Email successfully sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Notify about upcoming tasks
def notify_tasks():
    tasks = load_tasks("tasks.csv")
    today = datetime.now()
    next_week = today + timedelta(days=7)

    for task in tasks:
        if today <= task['due_date'] <= next_week:
            task_name = task['task_name']
            due_date = task['due_date'].strftime("%Y-%m-%d")
            email = task['email']

            message = (
                f"Hello,\n\n"
                f"This is a reminder for your upcoming task: {task_name}.\n"
                f"The due date is {due_date}. Please ensure it is completed on time.\n\n"
                f"Best regards,\nTask Reminder Bot"
            )

            send_email(email, f"Task Reminder: {task_name}", message)

# Schedule the notification to run weekly
schedule.every().monday.at("09:00").do(notify_tasks)

print("Task reminder scheduler started.")

# Run the scheduler
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Scheduler stopped.")
