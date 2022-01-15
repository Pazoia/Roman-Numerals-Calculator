from src.calculator import Calculator

def test_addition_of_two_roman_numerals():
    calculator = Calculator()
    assert calculator.add("I", "I") == "II"

def test_multiplication_of_two_roman_numerals():
    calculator = Calculator()
    assert calculator.multiply("II", "V") == "X"

def test_subtraction_of_two_roman_numerals():
    calculator = Calculator()
    assert calculator.subtract("V", "I") == "IV"

def test_division_of_two_roman_numerals():
    calculator = Calculator()
    assert calculator.divide("IV", "II") == "II"

def test_result_is_between_11_and_19():
    calculator = Calculator()
    assert calculator.add("X", "IV") == "XIV"

def test_result_is_20():
    calculator = Calculator()
    assert calculator.add("X", "X") == "XX"