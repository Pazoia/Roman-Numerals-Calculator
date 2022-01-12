from src.helper_functions import get_key

def test_get_key_function_return_key_from_a_chosen_value():
    test_dict = {
        "test_1": 1,
        "test_2": 2,
        "test_3": 3,
    }
    assert get_key(2, test_dict) == "test_2"