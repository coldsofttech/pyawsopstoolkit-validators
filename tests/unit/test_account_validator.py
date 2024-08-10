import unittest

from pyawsopstoolkit_validators.account_validator import number
from pyawsopstoolkit_validators.exceptions import ValidationError


class TestAccountValidator(unittest.TestCase):
    def test_number_valid(self):
        numbers = {
            "Number1": "123456789012"
        }

        for key, value in numbers.items():
            self.assertTrue(number(value, custom_error_message=f'{key} is not valid.'))

    def test_number_invalid(self):
        numbers = {
            "Number1": "123",
            "Number2": "01234567890123",
            "Number3": 123456789012
        }

        for key, value in numbers.items():
            with self.assertRaises(Exception) as context:
                number(value)

            self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))


if __name__ == "__main__":
    unittest.main()
