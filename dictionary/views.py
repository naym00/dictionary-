from word import models as MODELS_WORD
from word_meaning import models as MODELS_MEAN
from example import models as MODELS_EXAM
from user import models as MODELS_USER
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from word.serializers.GET import serializer as SR_WORD

def home(request):
    html_path = 'dictionary/home.html'
    context = {
        'title': 'Home',
        'user': request.user
    }
    return render(request, html_path, context=context)