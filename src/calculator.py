from .roman_numerals import roman_numerals_to_integer
from .roman_numerals import integer_to_roman_numerals

class Calculator:
    
    def add(roman_num_1, roman_num_2):
        result = roman_numerals_to_integer[roman_num_1] + roman_numerals_to_integer[roman_num_2]
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


    def multiply(roman_num_1, roman_num_2):
        result = roman_numerals_to_integer[roman_num_1] * roman_numerals_to_integer[roman_num_2]
        return integer_to_roman_numerals[result]

    def subtract(roman_num_1, roman_num_2):
        result = roman_numerals_to_integer[roman_num_1] - roman_numerals_to_integer[roman_num_2]
        return integer_to_roman_numerals[result]

    def divide(roman_num_1, roman_num_2):
        result = roman_numerals_to_integer[roman_num_1] / roman_numerals_to_integer[roman_num_2]
        return integer_to_roman_numerals[result]

    