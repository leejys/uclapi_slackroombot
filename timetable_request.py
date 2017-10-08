import json
import requests

def personal_timetable(OAUTH_TOKEN, CLIENT_SECRET):
    params = {
      "token": OAUTH_TOKEN,
      "client_secret": CLIENT_SECRET,
    }


    r = requests.get("https://uclapi.com/timetable/personal", params=params)
    timetable = r.json()
    #print(timetable)
    return(timetable)

#personal_timetable()

