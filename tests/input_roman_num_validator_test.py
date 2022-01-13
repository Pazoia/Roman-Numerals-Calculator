from src.input_roman_numeral_validator import roman_num_validator

def test_returns_correct_integer_when_in_roman_numerals_to_integer():
    assert roman_num_validator("I") == 1
    assert roman_num_validator("IV") == 4
