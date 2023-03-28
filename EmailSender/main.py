from email.message import EmailMessage
import ssl
import smtplib

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file


def send_email():
    """
    Send email with a fixed value via my gmail
    """
    APP_PASSWORD = os.getenv("APP_PASSWORD")
    EMAIL_SENDER = os.getenv("EMAIL_SENDER")
    EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
    EMAIL_PASSWORD = APP_PASSWORD

    if not EMAIL_PASSWORD:
        raise ValueError("APP_PASSWORD is not set correctly in environment variables")

    if not EMAIL_SENDER or not EMAIL_RECEIVER:
        raise ValueError(
            "EMAIL_SENDER or EMAIL_RECEIVER is not set correctly in environment variables"
        )

    subject = "This is the email subject"
    body = "This is the email body"

    em = EmailMessage()
    em["From"] = EMAIL_SENDER
    em["To"] = EMAIL_RECEIVER
    em["subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, em.as_string())
