from celery import shared_task
import time

from django.core.mail import send_mail

from .models import Animal


@shared_task
def save_animal():
    time.sleep(10)
    animals = Animal.objects.all()
    with open('result.txt', 'w', encoding='utf-8') as f:
        for item in animals:
            f.write(item.name + '\n')


@shared_task
def send_mail_task(subject, text, email):
    send_mail(subject, text, 'leo@test.com', [email], fail_silently=False)
