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


def get_longest_call_duration_a_number(calls):
    a_call_duration = {}
    for call in calls:
        cdr = parser.parse_record(call)

        if cdr.a_number in a_call_duration:
            a_call_duration[cdr.a_number] += cdr.duration
        else:
            a_call_duration[cdr.a_number] = cdr.duration

    a_number_longest = None
    a_number_longest_time = 0

    for a_number in a_call_duration.keys():

        if a_call_duration[a_number] > a_number_longest_time:
            a_number_longest_time = a_call_duration[a_number]
            a_number_longest = a_number

    return a_number_longest, a_number_longest_time


def get_longest_call_duration_b_number(calls):
    b_call_duration = {}
    for call in calls:
        cdr = parser.parse_record(call)

        if cdr.b_number in b_call_duration:
            b_call_duration[cdr.b_number] += cdr.duration
        else:
            b_call_duration[cdr.b_number] = cdr.duration

    b_number_longest = None
    b_number_longest_time = 0

    for b_number in b_call_duration.keys():

        if b_call_duration[a_number] > b_number_longest_time:
            b_number_longest_time = b_call_duration[a_number]
            b_number_longest = b_number

    return b_number_longest, b_number_longest_time


a_number, a_number_total_time = get_longest_call_duration_a_number(calls)
b_number, b_number_total_time = get_longest_call_duration_b_number(calls)

if a_number_total_time > b_number_total_time:
    print(
        "{} spent the longest time, {} seconds, on the phone during September 2016.".format(
            a_number, a_number_total_time))
else:
    print(
        "{} spent the longest time, {} seconds, on the phone during September 2016.".format(
            b_number, b_number_total_time))
