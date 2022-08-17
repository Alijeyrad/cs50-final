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

@login_required
def index(request):
    return render(request, 'test_neo/build/index.html')

# @login_required
@csrf_exempt
def test_results(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    if request.method == "POST":

        results = json.loads(request.body.decode('utf-8'))

        # tests_collection.insert_one(results)
        
        return JsonResponse({"success": "ok"}, status=200)