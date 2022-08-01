from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Contact
from panel.models import User

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', False)
        email = request.POST.get('email', False)
        subject = request.POST.get('subject', False)
        message = request.POST.get('message', False)
    
        new_contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)

        user_with_email = User.objects.get(email=email)

        try:
            if request.user.is_authenticated:
                user = User.objects.get(id=request.user.id)
                new_contact.panel_user = user
                new_contact.is_user = True
            if not request.user.is_authenticated and user_with_email is not None:
                new_contact.panel_user = user_with_email
                new_contact.is_user = True

            new_contact.save()
        except:
            messages.error(request, "Something happened to the message you sent. Send it again please.")
            return HttpResponseRedirect(reverse('home:index'))

        messages.success(request, "Thank you for contacting us. We'll get back to you as soon as possible.")
        return HttpResponseRedirect(reverse('home:index'))
