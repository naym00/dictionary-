from django.contrib import admin
from word import models as MODELS_WORD

admin.site.register([
    MODELS_WORD.Complexitylevel,
    MODELS_WORD.Word
])