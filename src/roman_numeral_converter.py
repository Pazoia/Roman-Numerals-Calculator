from src.roman_numerals import roman_numerals_to_integer
from functools import reduce

class Converter:
    def __init__(self):
        self.values = []

    def convert_roman_num_to_int(self, roman_num):
        
        def split(word):
            return list(word)

        roman_num_breakdown = split(roman_num)
        
        for i in range(len(roman_num_breakdown)):
            if len(roman_num_breakdown) == 0:
                break

            if len(roman_num_breakdown) == 1:
                self.values.append(roman_numerals_to_integer[roman_num_breakdown[0]])
                roman_num_breakdown.remove(roman_num_breakdown[0])
                break

            paired_chars = f"{roman_num_breakdown[0]}{roman_num_breakdown[1]}"
            
            if paired_chars not in roman_numerals_to_integer:
                self.values.append(roman_numerals_to_integer[roman_num_breakdown[0]])
                roman_num_breakdown.remove(roman_num_breakdown[0])

            if paired_chars in roman_numerals_to_integer and len(roman_num_breakdown) <= 2:
                self.values.append(roman_numerals_to_integer[paired_chars])
                roman_num_breakdown.remove(roman_num_breakdown[0])
                roman_num_breakdown.remove(roman_num_breakdown[0])
                break
            elif paired_chars in roman_numerals_to_integer:
                self.values.append(roman_numerals_to_integer[paired_chars])
                roman_num_breakdown.remove(roman_num_breakdown[0])
                roman_num_breakdown.remove(roman_num_breakdown[0])

        return reduce(lambda x, y: x+y, self.values)
