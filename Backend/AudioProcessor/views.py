from django.shortcuts import render
from django.http import HttpResponse
import base64
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import azure_functions
from .constants import *

# Create your views here.
def index(request):
    return HttpResponse("Hey! This is the Heatmap Back Health Check Endpoint! All looks good here!")

class send_audio(APIView):
    """
        GET: Update Location of a driver in database
    """
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        """
        :return: Health API check
        """

        import ipdb; ipdb.set_trace()
        mp3_data = base64.b64decode(audio)
        azure_functions.start(mp3_data)
        return Response({'status': 'All good!'}, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        :return: Update Driver Location
        """
        import ipdb; ipdb.set_trace()
        data = request.data
        mp3_data = base64.b64decode(request.data['key'])
        client_id = request.data['cid']
        meeting_id = request.data['mid']
        azure_functions.start(client_id, mp3_data)
        print(request.data)
        return Response({'toast_text': 'aa gaya'}, status=status.HTTP_200_OK)

