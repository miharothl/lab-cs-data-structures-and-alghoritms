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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

parser = CdrParser()

"""
Create a set of possible telemarketers:
these are numbers that make outgoing calls
but never
 send texts,
 receive texts
 receive incoming calls
"""
#####################################################################################################################

unique_a_call_numbers = {}
unique_b_call_numbers = {}
unique_a_text_numbers = {}
unique_b_text_numbers = {}

for call in calls:
    cdr = parser.parse_record(call)

    unique_a_call_numbers[cdr.a_number] = "record"
    unique_b_call_numbers[cdr.b_number] = "record"

for text in texts:
    tdr = parser.parse_record(text)

    unique_a_text_numbers[tdr.a_number] = "record"
    unique_b_text_numbers[tdr.b_number] = "record"

unique_a_call_numbers = list(unique_a_call_numbers.keys())
unique_b_call_numbers = list(unique_b_call_numbers.keys())
unique_a_text_numbers = list(unique_a_text_numbers.keys())
unique_b_text_numbers = list(unique_b_text_numbers.keys())

marketing_candidates = []

for candidate in unique_a_call_numbers:

    candidate_flag = True

    for unique_b_call_number in unique_b_call_numbers:
        if candidate == unique_b_call_number:
            candidate_flag = False
            break

    for unique_a_text_number in unique_a_text_numbers:
        if candidate == unique_a_text_number:
            candidate_flag = False
            break

    for unique_b_text_number in unique_b_text_numbers:
        if candidate == unique_b_text_number:
            candidate_flag = False
            break

    if candidate_flag:
        marketing_candidates.append(candidate)


print("These numbers could be telemarketers: ")

for candidate in sorted(marketing_candidates):
    print(candidate)
