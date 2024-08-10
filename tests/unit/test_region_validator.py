import unittest

from pyawsopstoolkit_validators.exceptions import ValidationError
from pyawsopstoolkit_validators.region_validator import region


class TestRegionValidator(unittest.TestCase):
    def test_region_valid(self):
        regions = {
            "Region1": "us-east-1",
            "Region2": "af-south-1",
            "Region3": "ap-northeast-1"
        }

        for key, value in regions.items():
            self.assertTrue(region(value, custom_error_message=f'{key} is not valid.'))

    def test_region_invalid(self):
        regions = {
            "Region1": "usa-east-1",
            "Region2": "usa-east1-1",
            "Region3": "us-eas-1",
            "Region4": "us-east-12"
        }

        for key, value in regions.items():
            with self.assertRaises(Exception) as context:
                region(value)

                self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))


if __name__ == "__main__":
    unittest.main()
