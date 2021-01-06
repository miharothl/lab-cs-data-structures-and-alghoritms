"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

from telecom.cdr_parser import CdrParser

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

parser = CdrParser()


def get_longest_call_duration_number(calls):
    call_duration = {}
    for call in calls:
        cdr = parser.parse_record(call)

        if cdr.a_number in call_duration:
            call_duration[cdr.a_number] += cdr.duration
        else:
            call_duration[cdr.a_number] = cdr.duration

        if cdr.b_number in call_duration:
            call_duration[cdr.b_number] += cdr.duration
        else:
            call_duration[cdr.b_number] = cdr.duration

    number_longest = None
    number_longest_time = 0

    for number in call_duration.keys():

        if call_duration[number] > number_longest_time:
            number_longest_time = call_duration[number]
            number_longest = number

    return number_longest, number_longest_time


number, number_total_time = get_longest_call_duration_number(calls)

print(
    "{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    number, number_total_time))
