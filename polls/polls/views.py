from django.shortcuts import render
from django.http import httpResponse
# create your views here.
def index(request):
    return httpResponse("hello,world")