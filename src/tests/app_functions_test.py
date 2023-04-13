import unittest
import app_functions


class TestAppFunctions(unittest.TestCase):
    def setUp(self):
        print("setup")

    def test_get_new_quote_returns_something(self):
        result = app_functions.AppFunctions().get_new_quote()
        content_length = len(result[0])
        self.assertTrue(content_length > 0)


#TestAppFunctions().test_get_new_quote_returns_something()
