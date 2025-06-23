from django.contrib import admin
from word_meaning import models as MODELS_MEAN

admin.site.register([
    MODELS_MEAN.Wordmeaning
])