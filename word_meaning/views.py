from word import models as MODELS_WORD
from word_meaning import models as MODELS_MEAN
from example import models as MODELS_EXAM
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from word.serializers.GET import serializer as SR_WORD

def add_word_meaning(request, word_id=None):
    if request.method == 'POST':
        meaning = request.POST.get('meaning')
        word_instance = MODELS_WORD.Word.objects.get(id=word_id)
        if meaning.strip():
            MODELS_MEAN.Wordmeaning.objects.create(text=meaning, word=word_instance)
    return redirect('preview-words')

def edit_word_meaning(request, id=None):
    if request.method == 'POST':
        meaning = request.POST.get('meaning')
        MODELS_MEAN.Wordmeaning.objects.filter(id=id).update(text=meaning)
    return redirect('preview-words')
    
def delete_word_meaning(request, id=None):
    MODELS_MEAN.Wordmeaning.objects.get(id=id).delete()
    return redirect('preview-words')