from math import floor


class Integer:

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, roman_value: str):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(roman_value):
            if (i + 1) == len(roman_value) or roman_numerals[c] >= roman_numerals[roman_value[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return cls(result)

    @classmethod
    def from_string(cls, string_value):
        if not isinstance(string_value, str):
            return "wrong type"
        try:
            num = int(string_value)
            return cls(num)
        except ValueError:
            return "wrong type"
