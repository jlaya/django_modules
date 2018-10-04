from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep


@shared_task()
def enviar_email():
    import time
    print("iniciar envio de email....")
    repeats = range(8)
    for n_repeats in repeats:
        time.sleep(1)
        print("{0} sec. ".format((n_repeats+1)))

