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
        
        for i in range(len(roman_num_breakdown)):
            if len(roman_num_breakdown) == 0:
                break

            if len(roman_num_breakdown) == 1:
                values.append(roman_numerals_to_integer[roman_num_breakdown[0]])
                roman_num_breakdown.remove(roman_num_breakdown[0])
                break

            paired_chars = f"{roman_num_breakdown[0]}{roman_num_breakdown[1]}"
            
            if paired_chars not in roman_numerals_to_integer:
                values.append(roman_numerals_to_integer[roman_num_breakdown[0]])
                roman_num_breakdown.remove(roman_num_breakdown[0])

            if paired_chars in roman_numerals_to_integer and len(roman_num_breakdown) <= 2:
                values.append(roman_numerals_to_integer[paired_chars])
                roman_num_breakdown.remove(roman_num_breakdown[0])
                roman_num_breakdown.remove(roman_num_breakdown[0])
                break
            elif paired_chars in roman_numerals_to_integer:
                values.append(roman_numerals_to_integer[paired_chars])
                roman_num_breakdown.remove(roman_num_breakdown[0])
                roman_num_breakdown.remove(roman_num_breakdown[0])

        return reduce(lambda x, y: x+y, values)
