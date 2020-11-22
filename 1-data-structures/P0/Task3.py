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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

parser = CdrParser()

#####################################################################################################################
# A

fixed_area_codes = {}

for call in calls:
    cdr = parser.parse_record(call)

    fixed_area_code = cdr.is_fixed(cdr.a_number)

    if fixed_area_code is not None:
        fixed_area_codes[fixed_area_code] = "record"

    fixed_area_code = cdr.is_fixed(cdr.b_number)

    if fixed_area_code is not None:
        fixed_area_codes[fixed_area_code] = "record"

fixed_area_codes = list(fixed_area_codes.keys())

print("The numbers called by people in Bangalore have codes:")
for fixed_area_code in sorted(fixed_area_codes):
    print(fixed_area_code)

#####################################################################################################################
# B

num_calls = 0
num_fixed_to_fixed_calls = 0

for call in calls:
    cdr = parser.parse_record(call)

    fixed_area_code_a = cdr.is_fixed(cdr.a_number)
    fixed_area_code_b = cdr.is_fixed(cdr.b_number)

    if fixed_area_code_a and fixed_area_code_b:
        num_fixed_to_fixed_calls += 1

    num_calls += 1

print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(num_fixed_to_fixed_calls/num_calls*100))

