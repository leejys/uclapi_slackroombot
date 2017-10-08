#module for people
import json
import requests

def get_people(query, UCL_API_TOKEN):

    params = {
      "token": UCL_API_TOKEN,
      "query": query
    }

    url = "https://uclapi.com/search/people"
    r = requests.get(url, params=params)
    #people_data = "People found: "
    people = r.json()
    extracted = people['people']
    everything = []

    for person in extracted:
        person_data = "{} ({}) in the {}: {}".format(
            person["name"],
            person["status"],
            person["department"],
            person["email"]
        )
        everything.append(person_data)
        #print(person_data)
    #returns a list
    return(everything)    
