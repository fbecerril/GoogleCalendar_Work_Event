# GoogleCalendar_Work_Event
This program's intent is to take in input from a work schedule to be added onto my personal Google Calendar.

My work week schedule is sent to me through email, when copying the raw text onto a txt file I can get my schedule formated as:

MON:
06/08	05:45pm-02:15am
TUE:
06/09	05:45pm-02:15am
WED:
06/10	OFF
THU:
06/11	05:45pm-02:15am
FRI:
06/12	06:15pm-02:30am
SAT:
06/13	11:00am-07:30pm
SUN:
06/14	10:00am-06:30pm

The program will ignore any lines that isn't exactly 21 in length
It expects for input to be in the format of xx/xx xx:xxpm-xx:xxpm
We take each string input change it into 24hr format and enter it into a google event template
Then we create a google event for every valid input given

#Future Updates
-decide what color the event will be
-reduce code size
-choose google calendar
-




