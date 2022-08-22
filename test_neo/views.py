import json
from uuid import uuid4
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from utils import tests_collection, rate_answer
from panel.models import User

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

        # add uuid
        results["u_id"] = uuid4().hex

        # insert into mongodb
        tests_collection.insert_one(results)


        return JsonResponse({"success": "ok"}, status=200)


@login_required
def show_results(request, id):
    test = tests_collection.find_one({"u_id": id})
    user_id = test["user_id"]
    user = User.objects.get(id=user_id)
    openness = test["openness to experience"]
    return render(request, 'test_neo/results.html', {'test': test, 'user': user, 'openness': openness})


@csrf_exempt
@login_required
def send_results(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        test_id = data.get('test_id')
        doctor_username = data.get('doctor_username')
        doctor = User.objects.get(username=doctor_username)
        send = data.get('send')

        if send: # send
            query = { "u_id": test_id }
            new_value = {"$push": {"sent_to_doctors": doctor.username}}
            tests_collection.update_one(query, new_value)
            print('done')
        else: # unsend
            query = { "u_id": test_id }
            value = {"$pull": {"sent_to_doctors": doctor.username}}
            tests_collection.update_one(query, value)

        return JsonResponse({"success": "ok"}, status=200)
    else:
        return JsonResponse({"error": "Need PUT request"}, status=400)