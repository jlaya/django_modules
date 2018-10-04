from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import EmailForm
from .tasks import enviar_email


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                data['subject'],
                data['content'],
                'victormagallanes2@gmail.com',
                [data['to']],
                fail_silently=False,
            )
            enviar_email.delay()
            message = "Su correo fue enviado"
            return render(request, 'emails/send_email.html', {'message': message, 'form': form})
    else:
        form = EmailForm()
 
    return render(request, 'emails/send_email.html', {'form': form})
 

