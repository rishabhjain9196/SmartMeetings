import azure.cognitiveservices.speech as speechsdk
import os
import requests
import json
import sys
from constants import *
import numpy as np
from pydub import AudioSegment
from nlp import *

speech_key, service_region = "4b04ff41a23047a28ecd21af788f2bbc", "westus"
def get_auth_token():
    header = {
        'Content-type':'application/x-www-form-urlencoded',
        'Content-Length': '0',
        'Ocp-Apim-Subscription-Key': speech_key
        }
    response = requests.post(tokenUrl, headers=header)
    return response

def getText(filename):

    import ipdb; ipdb.set_trace()
    weatherfilename = appname + "/input_wav/" + filename
    authorization = 'Bearer ' + get_auth_token().text
    recoRequestHeader = {
        'Authorization' : authorization,
        # 'Transfer-Encoding' : 'chunked',
        'Content-type' : 'audio/wav; codec=audio/pcm; samplerate=16000'
        }
    
    base_dir = os.getcwd()
    audioBytes = open(os.path.join(base_dir,weatherfilename), 'rb').read()

    textGenerated = requests.post(SpeechServiceURI, headers=recoRequestHeader, data=audioBytes)
    data = json.loads(textGenerated.text)
    
    text = data.get('NBest', None)
    if text:
        text = text[0]['Display']
    return text

def convert_to_wav(path):
    import subprocess
    subprocess.call(['ffmpeg', '-i', path, path.replace('mp3', 'wav')])

def get_audio():
    return

def superimpose(paths, superimposed_path):
    sounds = []
    if len(paths) == 0:
        return null
    
    combined = AudioSegment.from_file(paths[0])
    
    for path in paths[1:]:
        current_sound = AudioSegment.from_file(path)
        sounds.append(current_sound)
        combined = combined.overlay(current_sound)
    
    combined.export(superimposed_path, format='wav')

def convert_to_text():
    # chunk creation
    # gettext for all chunks
    # combine chunked texts
    pass


def translations():
    pass

def send_meeting_mail():
    return

def delete_files():
    import os, shutil
    folder = '/path/to/folder'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

def start(id, mp3_data):
    # store mp3_data
    offset = appname + "/input_mp3/" + meeting_id + "/"
    meet_folder = os.path.join(os.getcwd(), offset)
    if not os.path.exists(meet_folder):
        os.makedirs(meet_folder)
    input_mp3_path = meet_folder + client_id + ".mp3"
    f = open(input_mp3_path, 'wb')
    f.write(mp3_data)
    f.close()
    
    #convert mp3 to wav
    paths = []
    for subdir, dirs, files in os.walk(meet_folder):
        for filename in files:
            if filename.endswith(".mp3"):
                # Assuming no directories inside the folder
                convert_to_wav(os.path.join(base_dir, filename))
    
    # # superimposing of wav files over one another and getting texts for all individual clients
    wav_offset = appname + "/input_wav" + meeting_id + "/"
    wav_meet_folder = os.path.join(os.getcwd(), wav_offset)
    paths = []
    count = 0
    base_dir = os.path.join(os.getcwd(), input_folder)
    for subdir, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith(".wav"):
                count = count + 1
                # Assuming no directories inside the folder
                paths.append(base_dir + "/" + filename)
    
    if count < 2:
        return {}
    
    superimpose(paths, os.path.join(os.getcwd(), wav_meet_folder) + '/superimposed.wav')

    # chunking of all wav audio files, superimposed file
    # input_folder = appname + "/input_wav"
    # paths = []
    # base_dir = os.path.join(os.getcwd(), input_folder)
    # for subdir, dirs, files in os.walk(base_dir):
    #     for filename in files:
    #         temp = 1
    #         if filename.endswith(".wav"):
    #             # Assuming no directories inside the folder
    #             import subprocess
    #             seg_time = '30'
    #             subprocess.call(['ffmpeg', '-i', os.path.join(base_dir, filename) , '-f', 'segment', '-segment_time', seg_time, '-c', 'copy', os.path.join(os.path.join(base_dir, str(temp)), "out.wav")])
    #         temp = temp + 1

    # calling get text for wav + superimposed
    dir = os.path.join(os.getcwd(), wav_meet_folder)
    texts = []
    clients = 2
    for dir, sub, files in os.walk(dir):
        texts.append(getText('input.wav'))
    # coverting text to moms

    # Create tasks via NLP -> Send Mail?
    x,y = processTranscript(fullText)
    # Meetings NLP

    # Transcipt

    # Translated Transcripts

    # stats
    return x + y

start()