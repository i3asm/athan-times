import requests
import pprint
import re

file = "data.json"

r = requests.get('http://api.aladhan.com/v1/timings/1398332113?latitude=51.508515&longitude=-0.1254872&method=4')

with open(file, 'w') as filetowrite:
    filetowrite.write(r.text)

