import unittest
import app_functions


class TestAppFunctions(unittest.TestCase):
    def setUp(self):
        print("setup")

    def test_get_new_quote(self):
        result = app_functions.AppFunctions().get_new_quote()
        
        self.assertEqual(result, len(result)>0)

