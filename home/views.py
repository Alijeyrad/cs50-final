from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request,'home/panel.html')
    else:
        return render(request, 'home/index.html')

def login_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home:panel'))

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home:panel'))
        else:
            return render(request, "home/index.html", {
                "message": "Invalid username or password! Try again.",
                "success": False
            })
    else:
        return render(request, "home/index.html")

def logout_view(request):
    logout(request)
    return render(request, 'home/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "home/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            # check if user is doctor or not
            if request.POST.get('is_doctor', False):
                user.is_doctor = True  
            user.save()
        except IntegrityError:
            return render(request, "home/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return render(request, "home/index.html")
    else:
        return render(request, "home/register.html")

@login_required
def panel(request):
    if request.user.is_authenticated:
        return render(request, "home/panel.html")
    else:
        return HttpResponseRedirect(reverse('home:index'))
        

@login_required
def profile(request):
    if request.user.is_authenticated:
        return render(request, "home/profile.html")
    else:
        return HttpResponseRedirect(reverse('home:index'))

@login_required
def profile_edit(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        # check password
        password = request.POST.get("password", False)
        confirmation = request.POST.get("confirmation", False)

        if password != confirmation:
            return render(request, "home/profile_edit.html", {
                'message': "Passwords Don't Match."
            })

        user_password = request.user.password
        password_is_right = check_password(password, user_password)

        if password_is_right:
            # get all the fields
            first_name = request.POST.get("first_name", False)
            last_name = request.POST.get("last_name", False)
            sex = request.POST.get("sex", False)
            username = request.POST.get("username", False)
            country = request.POST.get("country", False)
            city = request.POST.get("city", False)
            profile_pic = request.FILES.get('profile_pic', False)
            about = request.POST.get("about", False)

            # put the fields where they belong
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if sex:
                user.sex = sex
            
            # change Username

            if country:
                user.country = country
            if city:
                user.city = city
            if profile_pic:
                user.profile_pic = profile_pic
            if about:
                user.about = about
            
            user.save()
            return render(request, 'home/profile.html', {
                'message': 'Changes Saved.',
                'done': True
            })
        else:
            return render(request, "home/profile_edit.html", {
                'message': 'Wrong Password, Try Again.',
                'done': False
            })

    else:
        return render(request, "home/profile_edit.html")
        