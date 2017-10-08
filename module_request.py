import json
import requests

def module_timetable(string_code, OAUTH_TOKEN, CLIENT_SECRET):

    code = []
    code.append(string_code.upper())

    params = {
      "token": OAUTH_TOKEN,
      "client_secret": CLIENT_SECRET,
      "modules": code
    }

    r = requests.get("https://uclapi.com/timetable/bymodule", params=params)
    timetable = r.json()
    datetime_list = []
    lecturer_list = []
    module_list = []


    for i in timetable:
        module = timetable["timetable"]
        for event_date, details_list in sorted(module.items()):
            date = event_date
            for details in details_list:
                #not the best way to do this, it should only be done once
                module = details["module"]
                module_name = module["name"]
                module_code = module["module_code"]

                lecturer_name = module["lecturer"]["name"]
                lecturer_email = module["lecturer"]["email"]

                start_time = details["start_time"]
                end_time = details["end_time"]

                location = details["location"]
                location_combined = location["name"]

                timedate_entry = "{}: {} - {}, {}".format(date, start_time, end_time, location_combined)
                lecturer_entry = "Lecturer: {} ({})".format(lecturer_name, lecturer_email)
                 
                datetime_list.append(timedate_entry)
                lecturer_list.append(lecturer_entry)
                module_info = module_code + " " + module_name + "\n"  
                module_list.append(module_info)               

    entry_list = []
    #print(module_list)

    #append in a nice, readable way
    for i in datetime_list:
        for j in lecturer_list:
            combined_info = i + "\n" + j + "\n"
            entry_list.append(combined_info)

    #clean list and remove duplicate entries
    cleaned_list = list(set(entry_list))
    #for i in list(set(entry_list)):
    #    print(i)

    #obviously only do this if there were actually module names in the data obtained
    if len(module_list) > 0:
        cleaned_list.insert(0, module_list[0])
    return cleaned_list


