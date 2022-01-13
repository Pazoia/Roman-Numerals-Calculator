from src.calculator import Calculator

def test_addition_of_two_roman_numerals():
    assert Calculator.add("I", "I") == "II"

def test_multiplication_of_two_roman_numerals():
    assert Calculator.multiply("II", "V") == "X"

def test_subtraction_of_two_roman_numerals():
    assert Calculator.subtract("V", "I") == "IV"

def test_division_of_two_roman_numerals():
    assert Calculator.divide("IV", "II") == "II"

def test_result_is_between_11_and_19():
    assert Calculator.add("X", "IV") == "XIV"