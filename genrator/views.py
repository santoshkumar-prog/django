from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'genrator/home.html')

def about(request):
    return render(request, 'genrator/about.html')

def password(request):

    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        character.extend(list('12345678890'))


    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(character)


    return render(request, 'genrator/password.html', {'password':thepassword})
