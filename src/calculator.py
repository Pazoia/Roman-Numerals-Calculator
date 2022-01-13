from .roman_numerals import roman_numerals_to_integer
from .roman_numerals import integer_to_roman_numerals
from functools import reduce

class Calculator:

    def add(*args):
        values = []

        for roman_num in args:
            values.append(roman_numerals_to_integer[roman_num])
        
        result = reduce(lambda x, y: x+y, values)

        if result <= 10:
            return integer_to_roman_numerals[result]
        elif result > 10 and result <= 19:
            result_string = str(result)
            result_first_split = int(f"{result_string[0]}0")
            result_second_split = int(result_string[1])
            return f"{integer_to_roman_numerals[result_first_split]}{integer_to_roman_numerals[result_second_split]}"
        elif result >= 20:
            result_string = str(result)
            if result_string[1] == "0":
                result = ""
                for i in range(int(result_string[0])):
                    result += integer_to_roman_numerals[10]
                return result


    def multiply(*args):
        values = []
        
        for roman_num in args:
            values.append(roman_numerals_to_integer[roman_num])
        
        result = reduce(lambda x, y: x*y, values)
        return integer_to_roman_numerals[result]

    def subtract(*args):
        values = []
        
        for roman_num in args:
            values.append(roman_numerals_to_integer[roman_num])
        
        result = reduce(lambda x, y: x-y, values)
        return integer_to_roman_numerals[result]

    def divide(*args):
        values = []
        
        for roman_num in args:
            values.append(roman_numerals_to_integer[roman_num])
        
        result = reduce(lambda x, y: x/y, values)
        return integer_to_roman_numerals[result]

    