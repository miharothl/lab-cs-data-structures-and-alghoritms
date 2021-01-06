"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

parser = CdrParser()

all_numbers = {}

for text in texts:
    tdr = parser.parse_record(text)

    all_numbers[tdr.a_number] = "record"
    all_numbers[tdr.b_number] = "record"

for call in calls:
    cdr = parser.parse_record(call)

    all_numbers[cdr.a_number] = "record"
    all_numbers[cdr.b_number] = "record"

print("There are {} different numbers in the records.".format(len(all_numbers.keys())))
