#Author: Francisco Becerril
#Format for input
#06/08	05:45pm-02:15am
#06/09	05:45pm-02:15am

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time
import datetime


#create event with start and end dates
def event_format(start, end):
    GMT_OFF = '-07:00'
    event_start = str(start + GMT_OFF)
    event_end = str(end + GMT_OFF)
    
    EVENT = {
        'summary':  'Work',
        'location': 'In-N-Out Burger, 2001 Alta Arden Expy, Sacramento, CA 95825, USA',
        'start':    {'dateTime': event_start},
        'end':      {'dateTime': event_end},
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 30},
                {'method': 'popup', 'minutes': 60},
            ],
        'colorId': '4',
        },
    }
    return EVENT

# Function to convert the date format
def convert24(str1):
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "am" and str1[:2] == "12":
        return "00" + str1[2:-2]

        # remove the AM
    elif str1[-2:] == "am":
        return str1[:-2]

        # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "pm" and str1[:2] == "12":
        return str1[:-2]

    else:
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:5]
#input check
def isTimeFormat(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False

def nextDay(start, end):
    if(int(start[:2]) > int(end[:2])):
        return True
    else:
        return False

def input_lines():
    print('What dates would you like to add?')
    line = input('Enter 0 to finish input\n')
    array = array[line]
    while(line != '0'):
        print('What dates would you like to add?')
        line = input('Enter 0 to finish input\n')
        array.append(line)
    return array

def dateToEvent(date):
    print(date)
    year = str(datetime.datetime.now().year)  # todays year
    month = date[:2]                    #month
    start_date = date[3:5]              #start day
    end_date = start_date               #end day
    start_time = date[6:13]             #start time
    end_time = date[14:21]              #end time


    if(len(date) == 21
    and isTimeFormat(start_time[:-2])
    and isTimeFormat(end_time[:-2])):
        formated_start_time = convert24(start_time)
        formated_end_time = convert24(end_time)

        #check if even ends until next day
        if(nextDay(formated_start_time, formated_end_time)):
            end_date = int(end_date) + 1
            end_date = str(f'{end_date:02}')

        # '2020-05-29T19:00:00' format for Gmail
        formated_start_date = str(year + '-' + month + '-' + start_date + 'T' + formated_start_time + ':00')
        formated_end_date = str(year + '-' + month + '-' + end_date + 'T' + formated_end_time + ':00')


        print(start_date + " " + formated_start_date)
        print(end_date + " " + formated_end_date)
        created_event = event_format(formated_start_date, formated_end_date)

        print('Added onto calendar')
        return created_event

    else:
        print('Wrong Format!')
        return -1


#get input
print('What dates would you like to add?')
line = input('Enter 0 to finish input\n')
array = []
while(line != '0'):
    array.append(line)
    line = str(input())
      
#set up calendar using Google API documentation
try:
    import argparse
    flags = argparse.ArgumentParser(parents = [tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)
CAL = build('calendar', 'v3', http=creds.authorize(Http()))

#create event for every valid date
for x in array:
    passed_event = dateToEvent(x)
    if(passed_event != -1):
        #add event to calendar
        e = CAL.events().insert(calendarId='calendar ID found under google calendar settings',
                                sendNotifications=False, body=passed_event).execute()
        print(''''**** %r event added:
            start:  %s
            End: %s''' % (e['summary'].encode('utf-8'),
                          e['start']['dateTime'], e['end']['dateTime']))

    else:
        print("Event was not added!")






