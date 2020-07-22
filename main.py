import requests
import json
import datetime

# file = "data.json"
# api = " http://api.aladhan.com/v1/timingsByCity?city=Riyadh&country=Saudi Arabia&method=4"
# r = requests.get(api)
# with open(file, 'w') as filetowrite:
#     filetowrite.write(r.text)
# loaded_json = json.loads(r.text)
# print(loaded_json["data"]["timings"])

class salah:
    def __init__(self, name, time):
        self.name = name
        self.time = time

# get salah from json
def getSalah(name, json):
    return json["data"]["timings"][name]

# format timedelta to have negative values
def format_timedelta(td):
    if td < datetime.timedelta(0):
        return '-' + format_timedelta(-td)
    else:
        return str(td)

# get time delta
def delta(salah):
    time = datetime.datetime.now().strftime("%H:%M")
    format = '%H:%M'
    return datetime.datetime.strptime(time, format) - datetime.datetime.strptime(salah, format)

# find the closest salah, and whether it's remaining time or past time
def closest(salawat):
    time = datetime.datetime.now().strftime("%H:%M")
    for salah in salawat:
        print(salah.name + ": " + salah.time)
        if (salah.time - time > 0):
            print("less")


file = open("data.json", "r")
loaded_json = json.load(file)

fajr = salah(name="fajr", time=format_timedelta(delta(getSalah("Fajr", loaded_json))))
dhuhr = salah(name="dhuhr", time=format_timedelta(delta(getSalah("Dhuhr", loaded_json))))
asr = salah(name="asr", time=format_timedelta(delta(getSalah("Asr", loaded_json))))
maghrib = salah(name="maghrib", time=format_timedelta(delta(getSalah("Maghrib", loaded_json))))
isha = salah(name="isha", time=format_timedelta(delta(getSalah("Isha", loaded_json))))

# print("fajr: " + format_timedelta(delta(getSalah("Fajr", loaded_json))))
# print("Dhuhr: " + format_timedelta(delta(getSalah("Dhuhr", loaded_json))))
# print("Asr: " + format_timedelta(delta(getSalah("Asr", loaded_json))))
# print("Maghrib: " + format_timedelta(delta(getSalah("Maghrib", loaded_json))))
# print("Isha: " + format_timedelta(delta(getSalah("Isha", loaded_json))))

salawat = {fajr, dhuhr, asr, maghrib, isha}

closest(salawat)
