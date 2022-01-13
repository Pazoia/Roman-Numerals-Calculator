from src.input_roman_numeral_validator import roman_num_validator

def test_returns_correct_integer_when_in_roman_numerals_to_integer():
    assert roman_num_validator("I") == 1
    assert roman_num_validator("IV") == 4

def test_when_not_in_roman_numerals_to_integer_and_roman_num_with_2_letters():
    assert roman_num_validator("XV") == 15
    assert roman_num_validator("XX") == 20
