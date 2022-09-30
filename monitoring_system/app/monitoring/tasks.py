from time import sleep
from celery import shared_task


@shared_task
def test_task():
    sleep(5)
    print('Ееее!')
