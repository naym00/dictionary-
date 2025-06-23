from rest_framework import serializers
from example import models as MODELS_EXAM

class Exampleserializer(serializers.ModelSerializer):
    class Meta:
        model = MODELS_EXAM.Example
        fields='__all__'