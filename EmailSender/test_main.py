import unittest

from unittest.mock import MagicMock, patch, ANY

from dotenv import load_dotenv
import os

# import the code that you want to test
from main import send_email


class TestEmailSending(unittest.TestCase):
    # Class method is a function defined inside a class, it can also be used with other instance that create from this class
    @classmethod
    def setUpClass(cls):
        # Load the environment variables from .env files
        load_dotenv()
        cls.APP_PASSWORD = os.getenv("APP_PASSWORD")
        cls.EMAIL_SENDER = os.getenv("EMAIL_SENDER")
        cls.EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

        if not cls.APP_PASSWORD:
            raise ValueError(
                "APP_PASSWORD is not set correctly in environment variables"
            )

        if not cls.EMAIL_SENDER or not cls.EMAIL_RECEIVER:
            raise ValueError(
                "EMAIL_SENDER or EMAIL_RECEIVER is not set correctly in environment variables"
            )

    def test_env_load_correctly(self):
        self.assertIsNotNone(self.APP_PASSWORD)
        self.assertIsNotNone(self.EMAIL_SENDER)
        self.assertIsNotNone(self.EMAIL_RECEIVER)

    # patch is use to mock the behavior of smtplib without actually sending the email
    @patch("smtplib.SMTP_SSL")
    def test_send_email(self, mock_smtp: MagicMock):
        send_email()
        mock_smtp.assert_called_once_with("smtp.gmail.com", 465, context=ANY)
        smtp_instance = mock_smtp.return_value.__enter__.return_value
        # Test if login is called
        smtp_instance.login.assert_called_once_with(
            self.EMAIL_SENDER, self.APP_PASSWORD
        )
        # Test if send mail is called
        smtp_instance.sendmail.assert_called_once_with(
            self.EMAIL_SENDER, self.EMAIL_RECEIVER, ANY
        )


if __name__ == "__main__":
    unittest.main()
