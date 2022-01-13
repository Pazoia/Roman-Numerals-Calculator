from .roman_numerals import roman_numerals_to_integer
from .roman_numerals import integer_to_roman_numerals

class Calculator:

    def add(*args):
        result = 0
        for roman_num in args:
            result += roman_numerals_to_integer[roman_num]
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
        result = 0
        for roman_num in args:
            result += roman_numerals_to_integer[roman_num]
        return integer_to_roman_numerals[result]

    def subtract(*args):
        result = 0
        for roman_num in args:
            result += roman_numerals_to_integer[roman_num]
        return integer_to_roman_numerals[result]

    def divide(*args):
        result = 0
        for roman_num in args:
            result += roman_numerals_to_integer[roman_num]
        return integer_to_roman_numerals[result]

    