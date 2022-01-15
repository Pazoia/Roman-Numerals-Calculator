from lib2to3.pytree import convert
from src.roman_numeral_converter import Converter
import pytest

@pytest.mark.parametrize("roman_num, expected_integer", [
    pytest.param("I", 1, id="when_in_roman_numerals_to_integer"),
    pytest.param("XV", 15, id="when_not_in_roman_numerals_to_integer_and_roman_num_with_2_chars"),
    pytest.param("XXIV", 24, id="when_not_in_roman_numerals_to_integer_and_last_number_of_the_result_is_4"),
    pytest.param("XXIX", 29, id="when_not_in_roman_numerals_to_integer_and_last_number_of_the_result_is_9"),
    pytest.param("XLIII", 43, id="when_not_in_roman_numerals_to_integer_and_first_number_of_the_result_is_4"),
    pytest.param("XCVIII", 98, id="when_not_in_roman_numerals_to_integer_and_first_number_of_the_result_is_9"),
])

def test_returns_correct_value(roman_num, expected_integer):
    converter = Converter()
    assert converter.convert_roman_num_to_int(roman_num) == expected_integer
