#Birthday Email Automator
#Objective: Send automated birthday wishes to friends and family

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Load the Excel file
excel_file_path = "Birthday Tracker.xlsx"  # Update if file location changes
data = pd.read_excel(excel_file_path)

# Email configuration
EMAIL_ADDRESS = "ishanigiri7@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "bprv yrks wseb oskh"  # Replace with your email password
SMTP_SERVER = "smtp.gmail.com"            # Replace with your email provider's SMTP server
SMTP_PORT = 587                           # Replace with your email provider's port

# Current month
current_month = datetime.now().strftime("%m")

# Filter birthdays matching the current month
data['Month'] = data['BirthDay'].dt.strftime("%m")  # Add a 'Month' column
birthday_people = data[data['Month'] == current_month]

# Function to send an email
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
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Send birthday emails for the month
if not birthday_people.empty:
    for _, person in birthday_people.iterrows():
        name = person['Name']
        email = person['Email']
        dob = person['BirthDay'].strftime("%d-%b")  # Format as "Day-Month"
        message = (
            f"Dear {name},\n\n"
            f"Wishing you a very Happy Birthday on {dob}!\n\n"
            "May your month be filled with joy and celebrations.\n\n"
            "Best regards,\nYour Well-Wisher"
        )
        send_email(email, f"Upcoming Birthday Wishes for {name}!", message)
else:
    print("No birthdays this month!")
