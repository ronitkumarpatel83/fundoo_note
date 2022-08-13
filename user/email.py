from time import sleep
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


class Email:

    @staticmethod
    def send_email(email_list, mail_subject, mail_message):
        """Sends an email when the feedback form has been submitted."""
        sleep(20)  # Simulate expensive operation(s) that freeze Django
        mail = send_mail(mail_subject,
                         mail_message,
                         settings.EMAIL_HOST_USER,
                         email_list, fail_silently=False)
        return mail

    @classmethod
    def verify_user(cls, email, token):
        url = reverse("token_string", kwargs={"token": token})
        mail_subject = "Verification mail from celery"
        mail_message = f"Click on this {settings.BASE_URL}{url}"
        email_list = [email]
        cls.send_email(email_list, mail_subject, mail_message)

