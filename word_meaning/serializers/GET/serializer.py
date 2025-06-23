from rest_framework import serializers
from word_meaning import models as MODELS_MEAN

class Wordmeaningserializer(serializers.ModelSerializer):
    class Meta:
        model = MODELS_MEAN.Wordmeaning
        fields='__all__'