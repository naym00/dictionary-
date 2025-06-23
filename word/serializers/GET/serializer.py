from rest_framework import serializers
from word import models as MODELS_WORD
from word_meaning.serializers.GET.serializer import Wordmeaningserializer
from example.serializers.GET.serializer import Exampleserializer

class Complexitylevelserializer(serializers.ModelSerializer):
    class Meta:
        model = MODELS_WORD.Complexitylevel
        fields='__all__'

class Wordserializer(serializers.ModelSerializer):
    meanings = Wordmeaningserializer(many=True)
    examples = Exampleserializer(many=True)
    level = Complexitylevelserializer(many=False)
    date_time = serializers.SerializerMethodField('format_datetime')
    
    def format_datetime(self, instance):
        return instance.created_at 
    class Meta:
        model = MODELS_WORD.Word
        fields='__all__'