from src.roman_numerals import roman_numerals_to_integer

def roman_num_validator(roman_num):
    if roman_num in roman_numerals_to_integer:
        return roman_numerals_to_integer[roman_num]
