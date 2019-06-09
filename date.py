import sys
from datetime import date
import itertools


try:  # setting parameters to run on demanded configuration
    INPUT = sys.argv[1]
except IndexError:
    print('error: MISSING ARGUMENT[1]')
    INPUT = 'input.txt'


try:
    with open(INPUT, 'r') as input_text:  # opening file and closing after extracting data,
            # additional variables
            raw_data = input_text.readline()  # extracting first line from file
            input_data = (raw_data.split('/'))  # table to work with
            illegal = f'{raw_data} is illegal'  # output for illegal date
except FileNotFoundError:
    print('error: WRONG FILENAME OR DIRECTORY')


def to_int():  # converting list elements into integers to allow further processing
    for el in range(len(input_data)):
        input_data[el] = int(input_data[el])
    return input_data


def date_creator():
    to_int()
    input_data.sort()
    combinations_list = list(itertools.permutations(input_data, 3))  # creating list of every possible date combination
    result = date(9999, 9, 9)  # this variable will change value to the earliest legal date(if found)

    for n in range(len(combinations_list)):  # iterating through dates combinations
        # print(f'n = {n}')
        # uncomment the above to see at which iteration the earliest date was found
        try:
            if not (2000 < int(sum(combinations_list[n]))):  # checking if 4-digit year was provided in input,
                # if not then add 2000 to first element in combination sublist
                custom_year = int(combinations_list[n][0]) + 2000
            else:  # if provided, then continue - check if it can form valid date
                custom_year = int(combinations_list[n][0])
            temp_result = date(custom_year, int(combinations_list[n][1]), int(combinations_list[n][2]))
            # raises ValueError if sublist can't create valid date
            if temp_result < result and 2000 <= temp_result.year <= 2999:  # if date is valid, is the earliest one
                # and fits between Jan 1, 2000 and Dec 31, 2999 (inclusive), save as result
                result = temp_result

        except ValueError:
            failure = True

    if result != date(9999, 9, 9):  # if initial value is not changed, date matching requirements wasn't found
        return print(result)
    elif failure:
        return print(illegal)


date_creator()
