from django.db import models

class Settings(models.Model):
    otp_validation_minutes = models.IntegerField(default=2)
    def __str__(self):
        return f'{self.id} - {self.otp_validation_minutes}'