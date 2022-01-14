# Roman Numerals Calculator

# Client requirements

Build a calculator that takes roman numerals, and return the results also in roman numerals.

Results are always presented in Capital Letters

Edge cases:

If a user give lower case letter as the input.

> **input_roman_num_validator tests**

> input is in roman_numerals_to_integer dictionary

| Input | Output value |
| :---: | :----------: |
|   I   |    ✅ - 1    |

> input is not in roman_numerals_to_integer dictionary  
> input with multiple characters

| Input  | Output value |
| :----: | :----------: |
|   XV   |   ✅ - 15    |
|  XXIV  |   ✅ - 24    |
|  XXIX  |   ✅ - 29    |
| XLIII  |   ✅ - 49    |
| XCVIII |   ✅ - 98    |

"", 98

> **calculator tests**

|  Input  | Output Lower or equals to 10 |
| :-----: | :--------------------------: |
|  I + I  |           ✅ - II            |
| II \* V |            ✅ - X            |
|  V - I  |           ✅ - IV            |
| IV / II |           ✅ - II            |

|     Input     |        Output betwen 11 and 99        |
| :-----------: | :-----------------------------------: |
|    X + IV     | ✅ - ( XIV ) output between 11 and 19 |
|     X + X     |       ✅ - ( XX ) output is 20        |
|   X + XIII    |  ( XXIII ) output between 21 and 29   |
|    XX + X     |         ( XXX ) output is 30          |
|   X + XXVI    |  ( XXXVI ) output between 31 and 39   |
|   XV + XXV    |          ( XL ) output is 40          |
|   XX + XXVI   |   ( XLVI ) output between 41 and 49   |
|   XXV + XXV   |          ( L ) output is 50           |
|  XXX + XXIX   |   ( LIX ) output between 51 and 59    |
|    XL + XX    |          ( LX ) output is 60          |
| XXX + XXXVIII |  ( LXVIII ) output between 61 and 69  |
|    L + XX     |         ( LXX ) output is 70          |
| XL + XXXVIII  | ( LXXVIII ) output between 71 and 79  |
|    L + XXX    |         ( LXXX ) output is 80         |
|  L + XXXVII   | ( LXXXVII ) output between 81 and 89  |
|    XL + L     |          ( XC ) output is 90          |
|    L + XLV    |   ( XCV ) output between 91 and 99    |

# Technologies

- Python 3.8
- Pytest 5.4
