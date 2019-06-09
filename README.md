# Python-task-NEW-Milo-
Task description:
Assuming that you have a date in the "A/B/C" format, where A,B,C are integers
between 0 and 2999, we want you to output the earliest possible legal date between
Jan 1, 2000 and Dec 31, 2999 (inclusive) using them as day, month and year (but not
necessarily in that order).
Input:
* The input file consists of a single line containing three integers separated by "/".
* There are no extra spaces around the "/".
* Years may be truncated to two digits and may in that case also omit the leading 0 (if
there is one), so 2000 could be given as "2000", "00" or "0" (but not as an empty
string).
* Months and days may be zero-padded.
* You may assume that the year, when given with four digits, is between 2000 and 2999.
* At most one of the integers has four digits, and the others have one or two digits.

Output:
* Output a single line giving the earliest legal date possible given the above
constraints.
* The output should be formatted as year-month-day, where year has four digits, and
month and day have two digits each (zero padding), for example "2011-07-15".
* If there is no legal date (subject to the above constraints) then output a single line
with the original string followed by the words "is illegal".

# tech
* Python 3.7.2 
* Python standard library(sys, datetime, itertools)

# Instructions 
Place input.txt in the same directory as date.py

* Run with:
```
$ python date.py input.txt 
```
and get compliant result. 

* Run with: 
```
$ python date.py 
```
and get compliant result as well as error message (as far as input.txt is in the same directory as date.py, otherwise get error only ;) ) 

* Run with typo in input.txt, f.e:
```
$ python date.py input.txx 
```
and get error only. 

# note 
Functions take no arguments for they are written to do one job only(and with global variables). Howerver it's designed in such way to make the code reusable if needed(with a touch of refactoring).
