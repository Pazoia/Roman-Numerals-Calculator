from .roman_numerals import roman_numerals
from .helper_functions import get_key

class Calculator:
    
    def add(roman_num_1, roman_num_2):
        result = roman_numerals[roman_num_1] + roman_numerals[roman_num_2]
        return get_key(result, roman_numerals)

    def multiply(roman_num_1, roman_num_2):
        result = roman_numerals[roman_num_1] * roman_numerals[roman_num_2]
        return get_key(result, roman_numerals)

    def subtract(roman_num_1, roman_num_2):
        result = roman_numerals[roman_num_1] - roman_numerals[roman_num_2]
        return get_key(result, roman_numerals)

    def divide(roman_num_1, roman_num_2):
        result = roman_numerals[roman_num_1] / roman_numerals[roman_num_2]
        return get_key(result, roman_numerals)

    