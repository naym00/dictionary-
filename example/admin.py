from django.contrib import admin
from example import models as MODELS_EXAM

admin.site.register([
    MODELS_EXAM.Example
])