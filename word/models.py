from django.db import models
from user import models as MODELS_USER

class Complexitylevel(models.Model):
    text = models.CharField(max_length=50, unique=True)
    difficulty_level = models.IntegerField(default=1)
    color = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.id} - {self.difficulty_level} - {self.text}'

class Word(models.Model):
    user = models.ForeignKey(MODELS_USER.User, on_delete=models.CASCADE, related_name='user_words')
    text = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=100, blank=True, null=True)
    level = models.ForeignKey(Complexitylevel, on_delete=models.SET_NULL, null=True, blank=True, related_name='level_words')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id} - {self.text}'