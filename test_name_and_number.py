from unittest import TestCase
from name_and_number import name_and_phone_number, what_type_does_input_return, add_your_two_favorite_numbers


class Test(TestCase):
    def test_name_and_phone_number(self):
        self.assertEqual(name_and_phone_number(), f"Hello, , is  your phone number?")

    def test_what_type_does_input_return(self):
        self.assertEqual(what_type_does_input_return(), type(19))

    def test_add_your_two_favorite_numbers(self):
        self.assertEqual(add_your_two_favorite_numbers(), f"The sum of your favorite numbers is {7 + 19}")
