from django.shortcuts import render
from django.http import HttpResponse

from shiojia_api.app_initializer import api



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def trendAccount(request):
    print(api.list_accounts())
    return HttpResponse("OK")