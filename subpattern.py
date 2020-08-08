from protocols import cartesian_product, axis_Z
from complementary_variables import SPECIAL_CHAR

#
# Special Char Subpattern
#===========================================

def sc_forbegins():
    return SPECIAL_CHAR[4:5] + SPECIAL_CHAR[6:8] + SPECIAL_CHAR[12:14] + SPECIAL_CHAR[22:23]

def sc_forend():
    return SPECIAL_CHAR[2:3] + SPECIAL_CHAR[4:5] + SPECIAL_CHAR[7:8] + SPECIAL_CHAR[9:11] + SPECIAL_CHAR[23:24]

def sc_separator():
    return SPECIAL_CHAR[0:3] + SPECIAL_CHAR[12:14] + SPECIAL_CHAR[15:19]

def sc_separator_easy():
    return sc_separator()[0:3]

def sc_around():#retorna um objeto invés de uma lista
    return [
            [SPECIAL_CHAR[0], SPECIAL_CHAR[0]], 
            [SPECIAL_CHAR[4], SPECIAL_CHAR[4]],
            [SPECIAL_CHAR[19], SPECIAL_CHAR[20]],
            [SPECIAL_CHAR[13], SPECIAL_CHAR[13]],
            [SPECIAL_CHAR[7], SPECIAL_CHAR[7]]
           ]
#
# Number Subpattern
#===========================================

def number(size, number = 0, limit = 2020):
    number_of_algorithms = 1
    wordlist = []

    while True:
        wordlist.append(str(number))
        number += 1
        if not size >= len(str(number)) and not wordlist[-1] != str(limit):
            break
    return wordlist

def sample_sequence(end, begins = '1'):
    sequence = []

    for i in range(end):
        begins = begins + str(int(begins[-1]) + 1)
        sequence.append(begins)
    
    return sequence

def double_number():
    numbers_to_duplicate = number(2, 1, 99)
    return list(map(lambda a: a+a, numbers_to_duplicate))

def multi_number():
    numbers_to_multiplicate = number(1, 1, 9)
 
    number_one      = list(map(lambda a: a+a, numbers_to_multiplicate))
    number_two      = list(map(lambda a: a+a+a, numbers_to_multiplicate))
    number_three    = list(map(lambda a: a+a+a+a, numbers_to_multiplicate))
 
    return number_one + number_two + number_three

def striking_date():
    return number(4, 1991, 2021)

def common_number4():
    return double_number() + multi_number() + striking_date()
