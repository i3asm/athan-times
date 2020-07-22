import requests
import pprint
import re
import json
import datetime

date = datetime.datetime.now()

file = "data.json"
api = "http://api.aladhan.com/v1/calendarByCity?city=Riyadh&country=Saudi arabia&method=4&month="+str(date.month)+"4&year="+str(date.year)

r = requests.get(api)

loaded_json = json.loads(r.text)
print(loaded_json)

with open(file, 'w') as filetowrite:
    filetowrite.write(r.text)
