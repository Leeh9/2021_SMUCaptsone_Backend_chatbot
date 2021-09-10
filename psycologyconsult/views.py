from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Psycology
from .serializers import PsycologySerializer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json
from .psy_chatbot import bot_answer

@csrf_exempt
def chat_service(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        response = bot_answer(input1)
        output = dict()
        output['response'] = response
        return HttpResponse(json.dumps(output), status=200)
    else:
        return render(request, 'addresses/chat_test.html')