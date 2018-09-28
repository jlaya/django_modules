from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import EmailForm
 
		
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                data['to'],
                data['content'],
                'victormagallanes2@gmail.com',
                [data['email']],
                fail_silently=False,
            )
            return HttpResponseRedirect('/sendemail/')
    else:
        form = EmailForm()
 
    return render(request, 'emails/send_email.html', {'form': form})
 
# def thanks(request):
#     return render(request, 'thanks.html')
