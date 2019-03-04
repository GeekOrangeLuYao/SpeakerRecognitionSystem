import requests


url = ""

with open("./Resource/audio.wav", "rb") as fr:
    requests.post(url=url, data=fr)