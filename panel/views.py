import json
import math
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from utils import tests_collection
from .models import *

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request,'panel/panel.html')
    else:
        return render(request, 'panel/index.html')

def login_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('panel:panel'))

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('panel:panel'))
        else:
            return render(request, "panel/index.html", {
                "message": "Invalid username or password! Try again."
            })
    else:
        return render(request, "panel/index.html")

def logout_view(request):
    logout(request)
    return render(request, 'panel/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "panel/register.html", {
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
            return render(request, "panel/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return render(request, "panel/index.html")
    else:
        return render(request, "panel/register.html")

@login_required
def panel(request):
    if request.user.is_authenticated:
        return render(request, "panel/panel.html")
    else:
        return HttpResponseRedirect(reverse('panel:index'))      

@login_required
def profile(request):
    if request.user.is_authenticated:
        tests = tests_collection.find({"username": request.user.username}, {"_id": 0, "timestamp": 1, "u_id": 1})
        return render(request, "panel/profile.html", {'tests': tests})
    else:
        return HttpResponseRedirect(reverse('panel:index'))

@login_required
def settings(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        # check password
        password = request.POST.get("password", False)
        confirmation = request.POST.get("confirmation", False)

        if password != confirmation:
            messages.error(request, "Passwords Don't Match." )
            return HttpResponseRedirect(reverse('panel:settings'))

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
            about = request.POST.get("about", False)
            birth_date = request.POST.get("birth_date", False)

            # put the fields where they belong
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if sex:
                user.sex = sex
            if username:
                user.username = username
            if country:
                user.country = country
            if city:
                user.city = city
            if about:
                user.about = about
            if birth_date:
                user.birth_date = birth_date
            
            user.last_profile_update = now()
            user.save()
            messages.success(request, "Changes Saved." )
            return HttpResponseRedirect(reverse('panel:profile'))

        else:
            messages.error(request, "Wrong Password, Try Again." )
            return HttpResponseRedirect(reverse('panel:settings'))

    else:
        return render(request, "panel/settings.html")
        
@login_required
def change_password(request):
    if request.method == "POST":
        current_password = request.user.password
        new_password = request.POST.get('new_password', False)
        new_password_confirm = request.POST.get('new_password_confirm', False)

        old_password = request.POST.get('password', False)
        confirmation = request.POST.get('confirmation', False)

        if new_password != new_password_confirm:
            messages.error(request, "New Password and confirmation Don't Match." )
            return HttpResponseRedirect(reverse('panel:settings'))
        elif old_password != confirmation:
            messages.error(request, "Old Password and confirmation Don't Match." )
            return HttpResponseRedirect(reverse('panel:settings'))
        elif check_password(old_password, current_password) == False:
            messages.error(request, "Wrong Password! Try again." )
            return HttpResponseRedirect(reverse('panel:settings'))
        else:
            username = request.user.username
            u = User.objects.get(username=username)
            u.set_password(new_password)
            u.save()
            return render(request, 'panel/index.html', {'alert': 'Password Changed. Log In Again.'})

    else:
        return render(request, 'panel/settings.html')

@login_required
def change_picture(request):
    if request.method == "POST":
        password = request.POST.get("password", False)
        confirmation = request.POST.get("confirmation", False)
        user = User.objects.get(id=request.user.id)
        user_password = request.user.password
        profile_pic = request.FILES.get('profile_pic', False)

        if password != confirmation:
            messages.error(request, "Password and confirmation Don't Match." )
            return HttpResponseRedirect(reverse('panel:settings'))
        elif check_password(password, user_password) == False:
            messages.error(request, "Wrong Password! Try again." )
            return HttpResponseRedirect(reverse('panel:settings'))
        else:
            if profile_pic:
                user.photo = profile_pic
                user.save()
                messages.success(request, "Profile Picture Changed.")
                return HttpResponseRedirect(reverse('panel:profile')) 
            else:
                messages.error(request, "Sorry, Picture Not Changed.")
                return HttpResponseRedirect(reverse('panel:settings'))

    else:
        return render(request, 'panel/settings.html')

@login_required
def doctors(request):
    if request.user.is_doctor:
        return HttpResponseRedirect(reverse('panel:patients'))
    if not request.user.is_doctor:
        doctors = User.objects.all().filter(is_doctor=True)
        paginator = Paginator(doctors, 5) # show 5 doctors per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        number_of_pages = [x for x in range(1, page_obj.paginator.num_pages + 1)]

    return render(request, 'panel/doctors.html', {
        'page_obj': page_obj,
        'number_of_pages': number_of_pages,
    })

# a callback for users who are Doctors
# not a view
def is_doctor(user):
    return user.is_doctor

@login_required
@user_passes_test(is_doctor)
def patients(request):
    return render(request, 'panel/patients.html')

@login_required
def specialty(request):
    if request.method == 'POST':
        specialty = request.POST.get('specialty', False)
        password = request.POST.get('password', False)
        confirmation = request.POST.get('confirmation', False)

        if password != confirmation:
            messages.error(request, "Passwords Don't Match." )
            return HttpResponseRedirect(reverse('panel:settings'))

        user_password = request.user.password
        password_is_right = check_password(password, user_password)

        if specialty and password_is_right:
            new_doctor = Doctor(user=request.user, title=specialty)
            new_doctor.save()
            messages.success(request, "Specialty Set.")
            return HttpResponseRedirect(reverse('panel:profile'))
        else:
            messages.error(request, "Somthing Went Wrong! Try Again.")
            return HttpResponseRedirect(reverse('panel:settings'))

@login_required
def doctor_profile(request, id):
    doctor = User.objects.all().filter(pk=id).first()
    
    requesting_user = request.user
    user_follows_profile_owner = False
    for follow in doctor.followee.all():
        if follow.follower == requesting_user:
            user_follows_profile_owner = True

    return render(request, 'panel/doctor_profile.html', {
        'doctor': doctor,
        'user_follows_profile_owner': user_follows_profile_owner,
    })

@csrf_exempt
def follow_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    if request.method == "POST":
        data = json.loads(request.body)
        follower_username = str(data.get('follower'))
        followee_username = data.get('followee')
        follower = User.objects.get(username=follower_username)
        followee = User.objects.get(username=followee_username)
        follow_or_unfollow = data.get('follow')

        if follow_or_unfollow:
            follow_object = Follow.objects.create(follower=follower, followee=followee)
            follow_object.save()
        else:
            follow_object = Follow.objects.all().filter(follower=follower, followee=followee)
            follow_object.delete()

        return HttpResponse(status=204)

@login_required
def comment(request, id):
    if request.method == 'POST':
        doctor = User.objects.all().filter(id=id).first()
        writer = request.user
        content = request.POST.get('content', False)

        new_comment = Comment.objects.create(
            content = content,
            writer = writer,
            for_doctor = doctor
        )
        new_comment.save()
        messages.success(request, "Comment Posted. Thank You.")
        url = reverse('panel:doctor_profile', kwargs={'id': id})
        return HttpResponseRedirect(url)