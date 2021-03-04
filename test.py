import requests
import json
import base64
from apikey import saltlux_api_key as api

audio = open("sample_data_64kbps.mp3", 'rb')

audio_content = audio.read()
encoded_audio = base64.b64encode(audio_content).decode("utf-8")

audio.close()
# youtube = pyglet.media.load('sample_data_64kbps.mp3')

# URL 지정
url = api["url"]

# Header 정보 지정
headers = {'Content-Type': 'application/json; charset=utf-8'}

# Request Parameter 정보 지정
params = {
    "key": api["key"],
    "serviceId": "00750911590",
    "argument": {
        "audioData": encoded_audio
    }
}

response = requests.post(url, headers=headers, data=json.dumps(params))

print(response.content)

