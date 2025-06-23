from django.contrib import admin
from user import models as MODELS_USER

admin.site.register([
    MODELS_USER.User,
    MODELS_USER.Forgotpassword
])