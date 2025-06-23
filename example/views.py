from word import models as MODELS_WORD
from word_meaning import models as MODELS_MEAN
from example import models as MODELS_EXAM
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from word.serializers.GET import serializer as SR_WORD

def add_example(request, word_id=None):
    if request.method == 'POST':
        
        form_tobe_created = {'word': MODELS_WORD.Word.objects.get(id=word_id)}
        sentence = request.POST.get('sentence')
        if sentence: form_tobe_created.update({'sentence': sentence})
        translate_sentence = request.POST.get('translate_sentence')
        if translate_sentence: form_tobe_created.update({'translate_sentence': translate_sentence})
 
        MODELS_EXAM.Example.objects.create(**form_tobe_created)
    return redirect('preview-words')

def edit_example(request, id=None):
    if request.method == 'POST':
        form_tobe_edited = {}
        sentence = request.POST.get('sentence')
        if sentence: form_tobe_edited.update({'sentence': sentence})
        translate_sentence = request.POST.get('translate_sentence')
        if translate_sentence: form_tobe_edited.update({'translate_sentence': translate_sentence})
        MODELS_EXAM.Example.objects.filter(id=id).update(**form_tobe_edited)
    return redirect('preview-words')
    
def delete_example(request, id=None):
    MODELS_EXAM.Example.objects.get(id=id).delete()
    return redirect('preview-words')