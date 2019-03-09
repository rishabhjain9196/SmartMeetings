from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hey! This is the Heatmap Back Health Check Endpoint! All looks good here!")

def audio_to_transcript():
    return
