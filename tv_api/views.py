from django.shortcuts import render
from django.http import HttpResponse
import shioaji as sj
from shiojia_api.app_initializer import api
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def receive_alert(request):
    if request.method == 'POST':
        print(request.POST)
    return HttpResponse("Hello, world. You're at the polls index.")
