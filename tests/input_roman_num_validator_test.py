from src.input_roman_numeral_validator import roman_num_validator
import pytest

@pytest.mark.parametrize("roman_num, expected_integer", [
    pytest.param("I", 1, id="when_in_roman_numerals_to_integer"),
    pytest.param("XV", 15, id="when_not_in_roman_numerals_to_integer_and_roman_num_with_2_chars"),
    pytest.param("XXIV", 24, id="when_not_in_roman_numerals_to_integer_and_last_number_of_the_result_is_4"),
    pytest.param("XXIX", 29, id="when_not_in_roman_numerals_to_integer_and_last_number_of_the_result_is_9"),
    pytest.param("XLIII", 43, id="when_not_in_roman_numerals_to_integer_and_first_number_of_the_result_is_4"),
    pytest.param("XCVIII", 98, id="when_not_in_roman_numerals_to_integer_and_first_number_of_the_result_is_9"),
])

def test_returns_correct_integer(roman_num, expected_integer):
    assert roman_num_validator(roman_num) == expected_integer
