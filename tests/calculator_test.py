from src.calculator import Calculator

def test_addition_of_two_roman_numerals():
    assert Calculator.addition("I", "I") == "II"