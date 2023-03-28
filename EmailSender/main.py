from email.message import EmailMessage
import ssl
import smtplib

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file


def send_email():
    APP_PASSWORD = os.getenv("APP_PASSWORD")

    EMAIL_SENDER = "nguyenanhhao221@gmail.com"
    EMAIL_PASSWORD = APP_PASSWORD
    if not EMAIL_PASSWORD:
        raise ValueError("APP_PASSWORD is not set correctly in environment variables")

    EMAIL_RECEIVER = "hao@haonguyen.tech"

    subject = "This is the email subject"
    body = "This is the email body"

    em = EmailMessage()
    em["From"] = EMAIL_SENDER
    em["To"] = EMAIL_SENDER
    em["subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, em.as_string())
