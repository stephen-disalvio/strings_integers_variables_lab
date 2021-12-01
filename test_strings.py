from unittest import TestCase
from strings import this_is_a_string, string_variable_in_a_string


class Test(TestCase):
    def test_this_is_a_string(self):
        self.assertEqual(this_is_a_string(), type("a string"))

    def test_string_variable_in_a_string(self):
        self.assertEqual(string_variable_in_a_string(), "The value I assigned to my_string is: ?")