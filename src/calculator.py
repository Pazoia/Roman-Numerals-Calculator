from .roman_numerals import roman_numerals
from .roman_numerals import get_key

class Calculator:
    
    def addition(roman_num_1, roman_num_2):
        result = roman_numerals[roman_num_1] + roman_numerals[roman_num_2]
        print(result)
        return get_key(result)
    