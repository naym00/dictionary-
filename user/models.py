from django.db import models
from django.contrib.auth.models import AbstractUser
from help.choice import choice as CHOICE
from help.common.generic import ghelp


class User(AbstractUser):
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=ghelp.list_to_tuple(CHOICE.GENDER))
    
    @property
    def full_name(self):
        name = None
        if self.first_name and self.last_name: name = f'{self.first_name} {self.last_name}' 
        else:
            if self.first_name: name = self.first_name
            else:
                if self.last_name: name = self.last_name
        return name
    
    @property
    def short_name(self):
        name = None
        if self.first_name: name = self.first_name
        else:
            if self.last_name: name = self.last_name
        return name

    def __str__(self):
        return f'{self.username} - {self.is_superuser}'

class Forgotpassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_forgotpassword')
    otp = models.CharField(max_length=5, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.otp}'