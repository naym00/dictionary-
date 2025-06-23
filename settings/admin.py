from django.contrib import admin
from settings import models as MODELS_SETT

admin.site.register([
    MODELS_SETT.Settings,
])