from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Contact

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', False)
        email = request.POST.get('email', False)
        subject = request.POST.get('subject', False)
        message = request.POST.get('message', False)

        try:
            new_contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)
            new_contact.save()
        except:
            messages.success(request, "Something happened to the message you sent. Send it again please.")
            return HttpResponseRedirect(reverse('home:index'))

        messages.success(request, "Thank you for contacting us. We'll get back to you as soon as possible.")
        return HttpResponseRedirect(reverse('home:index'))
