from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return render(response, 'index.html')

def login_signup(response):
    return render(response, 'login_signup.html')