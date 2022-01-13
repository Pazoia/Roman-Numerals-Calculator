from .roman_numerals import roman_numerals_to_integer
from .roman_numerals import integer_to_roman_numerals

class Calculator:
    
    def add(roman_num_1, roman_num_2):
        result = roman_numerals_to_integer[roman_num_1] + roman_numerals_to_integer[roman_num_2]
        return integer_to_roman_numerals[result]

    def multiply(roman_num_1, roman_num_2):
        result = roman_numerals_to_integer[roman_num_1] * roman_numerals_to_integer[roman_num_2]
        return integer_to_roman_numerals[result]

    def subtract(roman_num_1, roman_num_2):
        result = roman_numerals_to_integer[roman_num_1] - roman_numerals_to_integer[roman_num_2]
        return integer_to_roman_numerals[result]

    def divide(roman_num_1, roman_num_2):
        result = roman_numerals_to_integer[roman_num_1] / roman_numerals_to_integer[roman_num_2]
        return integer_to_roman_numerals[result]

    