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

            if i == len(roman_num_breakdown) - 2:
                paired_chars = f"{roman_num_breakdown[i]}{roman_num_breakdown[i + 1]}"                
                if paired_chars in roman_numerals_to_integer:
                        values.append(roman_numerals_to_integer[paired_chars])
                        break
                else:
                    values.append(roman_numerals_to_integer[roman_num_breakdown[i]])
            else:
                    values.append(roman_numerals_to_integer[roman_num_breakdown[i]])

        print(values)
        return reduce(lambda x, y: x+y, values)

