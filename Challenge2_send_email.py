import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email():
    EMAIL_SENDER = "chetnabisht528@gmail.com"
    EMAIL_PASSWORD = "nwvc vzyr tifm btwi" 
    EMAIL_RECEIVER = "hr@ignitershub.com"

    subject = "Challenge 3 Completed"
    body = """Dear HR,

I have completed Challenge 3.

Name: Chetna Bisht
Semester: 8th
Branch: Computer Science & Engineering
Roll Number: 210180101016

Please find the required image attached.

Best regards,  
Chetna Bisht"""

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    image_path = r"C:\Users\hp\interns-assignments\myPhoto.jpeg"  
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            img = MIMEImage(img_file.read(), name=os.path.basename(image_path))
            msg.attach(img)
    else:
        print("Error: Image file not found. Please check the path.")
        return  

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: 
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

send_email()
