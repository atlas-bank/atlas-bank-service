import os

from services.api_request import ApiRequest

email_sender_function_url = os.getenv("VERCEL_EMAIL_SENDER_URL")

request = ApiRequest(email_sender_function_url)


class EmailService:

    @staticmethod
    def send_email(to: str, subject: str, body: str):
        data = {
            "to": to,
            "subject": subject,
            "body": body
        }
        request.post_request(data=data)
