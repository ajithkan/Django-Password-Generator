from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, request
import random
# Create your views here.

def home(request):
    return render(request, 'generator\index.html')

def password(request):
    thepassword=''
    chars = list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length'))
    if(request.GET.get('uppercase')):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if(request.GET.get('numbers')):
        chars.extend(list('0123456789'))
    if(request.GET.get('special')):
        chars.extend(list('!@#$%^&*()[],.;:\|/?+=_-'))
    for x in range(length):
        thepassword += random.choice(chars)
    return render(request, 'generator\password.html', {'password':thepassword})

def aboutus(request):
    return render(request, 'generator\aboutus.html')

def google(request):
    return render(request, 'generator\google.html')


