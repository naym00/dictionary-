from django.db import models
from word import models as MODELS_WORD


class Example(models.Model):
    sentence = models.CharField(max_length=100)
    translate_sentence = models.CharField(max_length=100)
    word = models.ForeignKey(MODELS_WORD.Word, on_delete=models.CASCADE, related_name='examples')
    def __str__(self):
        return f'{self.id} - {self.sentence}'