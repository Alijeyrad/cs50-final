import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from utils import tests_collection, rate_answer
from .models import *

# Create your views here.

@login_required
def index(request):
    return render(request, 'test_neo/build/index.html')


@login_required
@csrf_exempt
def test_results(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    if request.method == "POST":

        data = json.loads(request.body.decode('utf-8'))

        minutes = data.pop("minutes")
        seconds = data.pop("seconds")
        hours = data.pop("hours")
        # construct time string
        time = f"{hours}:{minutes}:{seconds}"

        # define variables
        results = {
            "agreeableness": 0,
            "extraversion": 0,
            "neuroticism": 0,
            "conscientiousness": 0,
            "openness to experience": 0
        }
        
        # get results from data
        for (k, v) in data.items():
            results[v["scale"]] += rate_answer(v["answer"], v["key"])

        # add user and time
        username = request.user.username
        user_id = request.user.id
        results["username"] = username
        results["user_id"] = user_id
        results["time"] = time

        # add timestamp
        results["timestamp"] = now()

        # insert into mongodb
        tests_collection.insert_one(results)


        return JsonResponse({"success": "ok"}, status=200)