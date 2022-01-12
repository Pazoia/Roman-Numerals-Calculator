from src.calculator import Calculator

def test_addition_of_two_roman_numerals():
    assert Calculator.add("I", "I") == "II"

def test_multiplication_of_two_roman_numerals():
    assert Calculator.multiply("II", "V") == "X"