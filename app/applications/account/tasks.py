import os

from config.celery import app
from django.core.mail import send_mail
from twilio.rest import Client


@app.task
def send_user_activation_link(email, activation_code):
    full_link = f'http://{os.environ.get("HOST")}:{os.environ.get("NGINX_PORT", "PORT")}' \
                f'/api/v1/account/activate/{activation_code}'
    send_mail(
        'from electronic store',
        f'Your activation link {full_link}',
        os.environ.get("EMAIL_HOST_USER"),
        [email]
    )


@app.task
def send_forgot_password_code(email, activation_code):
    send_mail(
        'from electronic store',
        f'Your code to change password {activation_code}',
        os.environ.get("EMAIL_HOST_USER"),
        [email]
    )


@app.task
def send_sms(text, receiver):
    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=text,
        from_='+13613155359',
        to=receiver
    )
