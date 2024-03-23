import unittest
from scripts.functions import parse_date, validate_email, get_valid_input, get_valid_date
from unittest.mock import patch
from datetime import datetime

class TestFunctions(unittest.TestCase):
    def test_parse_date(self):
        self.assertEqual(parse_date("01/01/2022"), datetime.date(datetime(2022, 1, 1)))
        with self.assertRaises(ValueError):
            parse_date("invalid date")

    def test_validate_email(self):
        self.assertEqual(validate_email("test@example.com"), "test@example.com")
        with self.assertRaises(ValueError):
            validate_email("invalid email")

    @patch('builtins.input', return_value='test')
    def test_get_valid_input(self, input):
        self.assertEqual(get_valid_input("Enter something: ", lambda x: x == 'test', "Error message"), 'test')

    @patch('builtins.input', return_value='01/01/2022')
    def test_get_valid_date(self, input):
        self.assertEqual(get_valid_date("Enter a date: "), datetime(2022, 1, 1))

if __name__ == '__main__':
    unittest.main()
