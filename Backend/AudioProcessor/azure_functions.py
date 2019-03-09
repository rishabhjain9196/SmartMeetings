import azure.cognitiveservices.speech as speechsdk
import os
import requests
import json
import sys
from . import constants
import numpy as np
from scikits.audiolab import wavread
from pydub import AudioSegment

speech_key, service_region = constants.speech_key, constants.service_region

def get_auth_token():
    header = {
        'Content-type':'application/x-www-form-urlencoded',
        'Content-Length': '0',
        'Ocp-Apim-Subscription-Key': speech_key
        }
    response = requests.post(constants.tokenUrl, headers=header)
    return response

def getText():
    weatherfilename = constants.appname + "/" + constants.filename
    authorization = 'Bearer ' + response.text
    recoRequestHeader = {
        'Authorization' : authorization,
        # 'Transfer-Encoding' : 'chunked',
        'Content-type' : 'audio/wav; codec=audio/pcm; samplerate=16000'
        }
    
    base_dir = os.getcwd()
    audioBytes = open(os.path.join(base_dir,weatherfilename), 'rb').read()

    textGenerated = requests.post(constants.SpeechServiceURI, headers=recoRequestHeader, data=audioBytes)
    data = json.loads(textGenerated.text)
    
    text = data.get('NBest', None)
    if text:
        text = text[0]['Display']
    return text

def convert_to_wav(path):
    sound = AudioSegment.from_mp3(path)
    path.replace('mp3', 'wav')
    sound.export(path, format="wav")

def get_audio():
    return

def superimpose(paths, superimposed_path):
    sounds = []
    if len(paths) == 0:
        return null
    
    combined = AudioSegment.from_file(path[0])
    
    for all path in paths[1:]:
        current_sound = AudioSegment.from_file(path)
        sounds.append(current_sound)
        combined = combined_sound.overlay(sound2)
    
    combined.export(superimposed_path, format='wav')

def convert_to_text():
    # chunk creation
    # gettext for all chunks
    # combine chunked texts

def translations():
    return

def send_meeting_mail():
    return
getText()