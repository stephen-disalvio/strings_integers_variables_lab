# You can run tests 1 at a time by pressing the green play button next to the test name
# When you run these tests, they will ask you for an input
# To give an input, you need to click in the run box below, after the prompt
# Enter your input, and press "Enter" for the test to continue
# You should make sure the input you enter matches the test expectation
# You will need to make your own test expectation for each test (after the orange comma ',')

from unittest import TestCase
from name_and_number import name_and_phone_number, what_type_does_input_return, add_your_two_favorite_numbers


class Test(TestCase):
    def test_name_and_phone_number(self):
        self.assertEqual(name_and_phone_number(), "expectation")

    def test_what_type_does_input_return(self):
        self.assertEqual(what_type_does_input_return(), "expectation")

    def test_add_your_two_favorite_numbers(self):
        self.assertEqual(add_your_two_favorite_numbers(), f"expectation: {7 + 19}")
