from src.input_roman_numeral_validator import roman_num_validator
import pytest

@pytest.mark.parametrize("roman_num, expected_integer", [
    pytest.param("I", 1, id="when_in_roman_numerals_to_integer"),
    pytest.param("XV", 15, id="when_not_in_roman_numerals_to_integer_and_roman_num_with_2_chars"),
])

def test_returns_correct_integer(roman_num, expected_integer):
    assert roman_num_validator(roman_num) == expected_integer
