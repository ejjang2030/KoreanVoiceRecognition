import requests
import json
import base64
from apikey import saltlux_api_key as api
import re

audio = open("sample_data_64kbps.mp3", 'rb')

# audio = open("sample_data_64kbps.mp3", 'rb')

# audio = open("sample_data_64kbps.wav", 'rb')  # wav 파일이며 sample data가 5MB 이상이다.
# 그래서 error_code는 ERROR_UNKOWN_SAMPLERATE_FILE

audio_content = audio.read()
encoded_audio = base64.b64encode(audio_content).decode("utf-8")
# print(encoded_audio)
audio.close()

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

jsonified_string = response.json()["content"]
# print(type(jsonified))
# print(jsonified_string)
list_str = jsonified_string.split('\n')
container = []
for c in list_str:
    con = re.split(" +", c)
    del con[0]
    container.append(con)
print(container)
