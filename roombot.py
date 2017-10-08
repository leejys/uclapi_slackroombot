#Slack bot for the UCL API, made as part of the UCL API hackathon in October 2017.
#Implements room search by capacity, people search, timetable by module and personal timetable.
#still very much a work in progress.
#Adapted from this tutorial: https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
import os
import time
import requests
import json
import re
from operator import itemgetter

from slackclient import SlackClient

#get all the settings
from settings import * 

from room_requests import get_rooms
from people_requests import get_people
from userdata_request import get_userdata
from timetable_request import personal_timetable
from module_request import module_timetable

#ucl token here
token = UCL_API_TOKEN

# starterbot's ID as an environment variable
#BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
#slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
slack_client = SlackClient(SLACK_BOT_TOKEN)


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Sorry, that was an invalid command. For help: @roombot help"
    #check what the command actually is.
    command_split = command.split()

    if command.startswith("help"):
        response = "Here are some commands you can use with the bot: \n @roombot get rooms - Get all rooms in the system. \n @roombot get rooms capacity <number> - Get all rooms with a minimum capacity of <number>. \n @roombot search people <person> - Search for a person by name. \n @roombot search people <email> - Search for a person by email. \n @roombot module timetable <module code> - Get the timetable for a particular module. \n @roombot my data - Get your UCL data. \n @roombot my timetable - Get your personal timetable. (do not recommend) \n"

    #STANDARD GREETING.
    elif command.startswith("hello"):
        response = "Greetings, human"

    #GETS ROOMS USING THE UCL API. ERROR HANDLING NOT IDEAL ATM, WILL FIX
    elif command.startswith("get rooms"):

        #reset the response thing 
        response = "Results: \n"

        #get rooms using the room request module
        response_unfiltered = get_rooms(UCL_API_TOKEN)

        #split everything by capacity etc
        unsorted_new = [i.split("//") for i in response_unfiltered]
        #print(new_list)
        new_list = sorted(unsorted_new, key = itemgetter(1))
        
        all_list = [i[0] for i in new_list]

        #NB: this error handling really isn't ideal, shouldn't waste time doing the entire request if there is an error to start with
        
        if len(command_split) > 2:
            if command_split[2] == "capacity" and len(command_split) > 3:
                try:
                    min_cap = int(command_split[3])        
                    filtered_list = [i[0] for i in new_list if int(i[1]) > min_cap]
                    #print(filtered_list)
                    for i in filtered_list:
                        response += i + '\n'  
                except ValueError:
                    #obviously invalid input so skip
                    #response += "ERROR: invalid input, must be an int. \n"
                    response = "Error, must be a valid int"
            else:
                response = "Error, please try again. Example: @roombot get rooms capacity 100"
                         
        else:
            for i in all_list:
                response += i + '\n'

    #search people functionality
    elif command.startswith("search people"):
        response = "People found: \n"

        #basically you must actually give it a name or it won't work
        #join the rest of the string and search for that
        if len(command_split) > 2:
            query = "".join(command_split[2:])
            response_raw = get_people(query, UCL_API_TOKEN)
            for i in response_raw:
                response += i + "\n"

        else:
            response = "You must enter a name or email address. Example: @roombot search people denise gorse. Alternatively, @roombot search people ucacdgo@ucl.ac.uk"       

    #get my own data functionality
    elif command.startswith("my data"):
        response = get_userdata(OAUTH_TOKEN_2, CLIENT_SECRET_2)

    #get module timetable
    #search people functionality
    elif command.startswith("module timetable"):

        #give it a module code or it won't work.
        #join the rest of the string and search for that
        #if len(command_split) > 2:
        response = "Module Timetable: \n"

        #basically you must actually give it a name or it won't work
        #join the rest of the string and search for that
        if len(command_split) > 2:
            query = "".join(command_split[2:])
            response_raw = module_timetable(query, OAUTH_TOKEN, CLIENT_SECRET)
            #print(response_raw)
            for i in response_raw:
                response += i + "\n"

        else:
            response = "Invalid command. Example: @roombot module timetable COMP3058"  
        

    #personal timetable functionality - this isn't really optimal right now
    elif command.startswith("my timetable"):
        response = personal_timetable(OAUTH_TOKEN, CLIENT_SECRET)

    #AFTER EVERYTHING ELSE
    #call the slack client and send the message
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True) 




def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("RoomBot is online!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed")
