from src.calculator import Calculator

def test_addition_of_two_roman_numerals():
    assert Calculator.add("I", "I") == "II"

def test_multiplication_of_two_roman_numerals():
    assert Calculator.multiply("II", "V") == "X"

def test_subtraction_of_two_roman_numerals():
    assert Calculator.subtract("V", "I") == "IV"