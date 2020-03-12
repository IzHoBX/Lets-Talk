import requests
import urllib

URL = "https://gpt2-reddit-dstdu4u23a-uc.a.run.app/"

params = {}
params['key1'] = input("keyword 1: ")
params['key2'] = input("keyword 2: ")
params['key3'] = input("keyword 3: ")

data = urllib.parse.urlencode(params)
print("loading")
res = requests.get(URL, data)
print(res.json()['text'])
