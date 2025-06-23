from rest_framework import serializers
from settings import models as MODELS_SETT

class Settingsserializer(serializers.ModelSerializer):
    class Meta:
        model = MODELS_SETT.Settings
        fields='__all__'