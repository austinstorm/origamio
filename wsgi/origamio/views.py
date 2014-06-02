import os
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/home.html')

def signin(request):
    return render_to_response('account/signin.html')

def signup(request):
    return render_to_response('account/signup.html')

def lost(request):
    return render_to_response('account/lost.html')

def 404(request):
    return render_to_response('home/404.html')