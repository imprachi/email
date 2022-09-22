from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings


def sendMail(request):
    messaeSent = False

    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sending an Email with Django"
            message = cd['message']

            send_mail((subject,message,settings.DEFAULT_FROM_EMAIL,[cd['recipient']]))
            messageSent = True

        else:
            form = EmailForm()
            return render(request, 'index.html',{
                'form': form,
                'messageSent':messaeSent,
            })
