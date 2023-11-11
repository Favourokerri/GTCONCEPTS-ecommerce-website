from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_mail_after_registration(email, auth_token):
    """ Function that handles email for verifying accounts after registration """
    subject = "Welcome to GT Concepts. Verify your account to log in"
    html_content = render_to_string('email/verify_account.html', {'auth_token': auth_token})
    msg = EmailMultiAlternatives(subject, 'Verify your account', settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()