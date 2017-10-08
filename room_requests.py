#separate module for the room request stuff
import json
import requests

def get_rooms(token):
    room_classification = {"LT":"Lecture Theatre", "CR":"Classroom", "SS":"Social Space", "PC1":"Public Cluster"}

    #why did i even do this
    building_codes = {'Front Lodges': '014', 'Roberts Building': '045', 'Medical Sciences and Anatomy': '016', 'Gordon Square, 16-18': '035', 'Rockefeller Building': '201', 'Gordon Street, 25': '002', 'IOE - Woburn Square, 18': '171', 'Drayton House': '107', 'IOE - John Adams Hall': '175', 'Physics Building': '006', 'Christopher Ingold Building': '067', 'Gordon Square, 20': '032', 'Gordon House': '088', 'Gordon Square, 22': '029', 'IOE - Bedford Way, 20': '162', 'Gordon Square, 26': '024', 'Gordon Square, 23': '028', 'Central House': '388', 'Engineering Front Building': '365', 'Chadwick Building': '013', 'New Quad Pop Up (Name not yet confirmed)': '440', 'Taviton Street 14-16': '126', 'Gordon Square, 31-34 & 14 Taviton St': '090', 'Cruciform Building': '212', 'IOE - Endsleigh Gardens, 9-11': '084', 'South Quad Pop Up Learning Hub': 'X402', 'Gordon Square, 25': '025', 'Birkbeck Malet Street': '180', 'Torrington Place, 1-19': '086', 'School of Pharmacy': '131', 'Foster Court': '040', 'DMS Watson Building': '042', 'Tottenham Court Road, 188': '363', 'Royal Free Hospital': '281', 'Main Building': '005', 'Chandler House': '235', 'Birkbeck Gordon Square, 43': '181', 'Pearson Building': '003', 'Medical School Building': '374', 'Medawar Building': '037', 'Darwin Building': '044', 'Bedford Way, 26': '085', 'Gordon Square, 24': '026', 'Malet Place Engineering Building': '350', 'South Wing': '012', 'Bernard Katz Building': '050'}
    
    params = {
        "token": token
        
    }
    url = "https://uclapi.com/roombookings/rooms"
    r = requests.get(url, params=params)
    rooms = r.json()
    #default if no results are found
    room_data = "No results found" 
    
    #listing of building names and site ids - get for later use
    everything = []
    for room in rooms["rooms"]:
        room_data = "{} ({}) in {} has a capacity of {}".format(
            room["roomname"],
            room_classification.get(room["classification"]),
            room["sitename"],
            room["capacity"]
        )
        #this just gets everything, filtering is done in the roombot script.
        #print(room_data)
        everything.append(room_data + "//" + str(room["capacity"]))
    return everything
        

 
if __name__ == "__main__":
    get_rooms()

