from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Psycology
from .serializers import PsycologySerializer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json
from .chatbot import bot_answer
@csrf_exempt
def chat_service(request):
    # if request.method == 'POST':
    #     input1 = JSONParser().parse(request)
    #     input1 = input1['input']
    #     print(input1)
    #     response = bot_answer(input1)
    #     output = dict()
    #     output['response'] = response
    #     return JsonResponse((output), status=200)

    if request.method == 'GET':
        input1 = request.GET['inputText']
        response = bot_answer(input1)
        output = dict()
        output['response'] = response
        return JsonResponse(output, safe=False, json_dumps_params={'ensure_ascii': False})
        
        #JsonResponse((output), status=200)

    else:
        HttpResponse(status=400)