from django.shortcuts import render
from email1.settings import EMAIL_HOST_USER
from webapp import forms
from django.core.mail import send_mail
    # Create your views here.
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Thanks for testing your mail'
        message = 'Wishing you A very very Happy New Year 2020 May your dreams all come True'
        recepient = str(sub['Email'].value())
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})