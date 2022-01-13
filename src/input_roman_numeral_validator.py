from src.roman_numerals import roman_numerals_to_integer
from functools import reduce

def roman_num_validator(roman_num):
    if roman_num in roman_numerals_to_integer:
        return roman_numerals_to_integer[roman_num]

    if roman_num not in roman_numerals_to_integer:
        def split(word):
            return list(word)

        values = []
        roman_num_breakdown = split(roman_num)
        
        for roman_num in roman_num_breakdown:
            values.append(roman_numerals_to_integer[roman_num])

        return reduce(lambda x, y: x+y, values)

