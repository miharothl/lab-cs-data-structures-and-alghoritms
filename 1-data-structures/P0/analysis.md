# Project 1: Unscramble Computer Science Problems

## Task 0: What is the first record of texts and what is the last record of calls?

### Input
* list of call records
* list of text records

### Output

* print last call record
* print first text record

### Algorithm

* load list of call records - N
* load list of text records - N
* access first text - 1
* access last call - 1

`N + N + 1 + 1 = 2N + 2 = O(N) <<-- algorithm is linear`

If loading of records is not included:

`1 + 1 = 2 = O(1) - algorithm is constant`

## Task 1: How many different telephone numbers are there in the records? 

### Input

* list of call records
* list of text records

### Output

* number of different telephone numbers 

### Algorithm

* load list of call records - N
* load list of text records - N
* traverse call records - N
* traverse text records - N

`N + N + N + N = 4N = O(N) <<-- algorithm is linear`


## Task 2: Which telephone number spent the longest time on the phone
during the period? 

### Input

* list of call records
* list of text records

### Output

* number spent longest time on the phone

### Algorithm

* load list of call records - N
* load list of text records - N
* traverse call records to sum a_number durations - N
* traverse unique a_numbers durations to find longest call- N
* traverse call records to sum b_number durations - N
* traverse unique b_numbers durations to find longest call- N

`N + N + N + N + N + N= 6N = O(N) <<-- algorithm is linear`

## Task 3A: Find all of the area codes and mobile prefixes called by people in Bangalore.

### Input

* list of call records
* list of text records

### Output

* ordered list of all area codes and mobile prefixes

### Algorithm

* load list of call records - N
* load list of text records - N
* traverse call records - N
* sort list of area codes - N * log N
* print list of sorted area codes - N

`N + N + N + N * log N + N = 5N + N * log N  = O(N * log N) <<-- algorithm is logaritmic`

## Task 3B: What percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore?  
 
### Input

* list of call records
* list of text records

### Output

* percentage of fixed calls

### Algorithm

* load list of call records - N
* load list of text records - N
* traverse call records - N
* calculate percentage of fixed calls = 1

`N + N + N + 1 = 3N + 1 = O(N) <<-- algorithm is linear`

## Task 4: The telephone company want to identify numbers that might be doing telephone marketing. 
 
### Input

* list of call records
* list of text records

### Output

* list of marketing candidates

### Algorithm

* load list of call records - N
* load list of text records - N
* traverse call records, to find unique a-call (candidate) and b-call numbers - N
* traverse text records, to find unique a-text and b-text - numbers - N
* for each candidate - N
  * traverse all b-call numbers - N
  * traverse all a-text numbers - N
  * traverse all b-text numbers - N
* sort list of candidates - N * log N
* print list of sorted area codes - N

`N + N + N + N + N * (N + N + N) + N * log(N) + N = 5N + (N * 3N) + (N * log N) = O(N^2) <<-- algorithm is exponential`

