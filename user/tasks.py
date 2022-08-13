import logging
from celery import shared_task
from .email import Email


@shared_task
def verify_user_task(email, token):
    try:
        Email.verify_user(email, token)
        return "Completed"
    except Exception as e:
        logging.exception(e)
