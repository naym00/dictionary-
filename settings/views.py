from settings.serializers.GET import serializer as SR_SETT
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from settings import models as MODELS_SETT
from help.common.generic import ghelp

@api_view(['GET'])
def get_settings(request):
    serialize_data = {}
    response_status = status.HTTP_400_BAD_REQUEST
    settings = ghelp.get_settings(MODELS_SETT.Settings)
    if settings:
        serialize_data = SR_SETT.Settingsserializer(settings, many=False).data
        response_status = status.HTTP_200_OK
    
    return Response(serialize_data, status=response_status)