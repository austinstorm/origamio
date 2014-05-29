import os
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/home.html')

def signin(request):
    return render_to_response('account/signin.html')