import unittest
from unittest.mock import patch
import json
import requests
from controller.app_functions import AppFunctions
from model.db_models import delete_user, delete_quote

class TestAppFunctions(unittest.TestCase):
    def setUp(self):
        self.username = "account"
        self.password = "password"
        self.quote = ['some random quote', 'author', "('random-quotes',)"]
        self.category = "All"
        delete_user(self.username)
        delete_quote(self.quote[0])

    def register(self):
        return AppFunctions().register(self.username, self.password)

    def test_get_new_quote_returns_data(self):
        result = AppFunctions().get_new_quote(self.category)
        content_length = len(result[0])
        self.assertTrue(content_length > 0)

    def test_get_new_quote_handles_timeout(self):
        with patch("controller.app_functions.requests.get", side_effect=requests.exceptions.Timeout):
            result = AppFunctions().get_new_quote(self.category)
            self.assertEqual((True, "Error: Connection timeout"), result)

    def test_get_new_quote_handles_connection_error(self):
        with patch("controller.app_functions.requests.get", side_effect=requests.exceptions.ConnectionError):
            result = AppFunctions().get_new_quote(self.category)
            self.assertEqual((True, "Error: Connection error"), result)

    def test_get_new_quote_handles_http_error(self):
        with patch("controller.app_functions.requests.get", side_effect=requests.exceptions.HTTPError):
            result = AppFunctions().get_new_quote(self.category)
            self.assertEqual((True, "Error: "), result)

    def test_get_new_quote_handles_json_decode_error(self):
        with patch("controller.app_functions.requests.get",
                    side_effect=json.JSONDecodeError("test message", "test doc", 0)):
            result = AppFunctions().get_new_quote(self.category)
            self.assertIn("Error decoding JSON: test message:", result[1])

    def test_get_new_quote_handles_key_error(self):
        with patch("controller.app_functions.requests.get") as mock_get:
            mock_response = mock_get.return_value
            mock_response.json.return_value = {}
            result = AppFunctions().get_new_quote(self.category)
            self.assertEqual((True, "The response data is missing"), result)

    def test_get_new_quote_partial_data_from_api(self):
        with patch("controller.app_functions.requests.get") as mock_get:
            mock_response = mock_get.return_value
            mock_response.json.return_value = [{
                "content": "",
                "author": "Test",
                "tags": ["Something"]
            }]
            result = AppFunctions().get_new_quote(self.category)
            self.assertEqual((True, "Some part of the response data is empty"), result)
    
    def test_response_returns_index_error(self):
        with patch("controller.app_functions.requests.get", side_effect=IndexError):
            result = AppFunctions().get_new_quote(self.category)
            self.assertEqual((True, "Index error while retrieving the data"), result)

    def test_response_is_not_empty_when_category_is_not_default(self):
        result = AppFunctions().get_new_quote("Sports")
        content_length = len(result[0])
        self.assertTrue(content_length > 0)
    
    def test_get_categories_returns_data(self):
        result = AppFunctions().get_categories()
        result_length = len(result)
        self.assertTrue(result_length > 0)
    
    def test_get_categories_value_error(self):
        with patch("controller.app_functions.requests.get", side_effect=ValueError):
            result = AppFunctions().get_categories()
            self.assertEqual((True, "An error occurred while retrieving the category data from the server: "), result)

    def test_get_categories_key_error(self):
        with patch("controller.app_functions.requests.get", side_effect=KeyError):
            result = AppFunctions().get_categories()
            self.assertEqual((True, "The categories data is missing"), result)

    def test_register_successful(self):
        result = self.register()
        self.assertTrue(result[0])
        delete_user(self.username)

    def test_register_fails_if_user_already_exists(self):
        self.register()
        result = AppFunctions().register(self.username, self.password)
        self.assertFalse(result[0])

    def test_register_fails_wihout_proper_password(self):
        result = AppFunctions().register(self.username, "")
        self.assertFalse(result)

    def test_register_fails_without_proper_username(self):
        result = AppFunctions().register("", self.password)
        self.assertFalse(result)

    def test_login_successful(self):
        self.register()
        result = AppFunctions().login(self.username, self.password)
        self.assertTrue(result)

    def test_login_fails_with_false_password(self):
        self.register()
        result = AppFunctions().login(self.username, "")
        self.assertFalse(result[0])

    def test_login_fails_with_false_username(self):
        self.register()
        result = AppFunctions().login("", self.password)
        self.assertFalse(result[0])

    def test_add_quote_successful(self):
        self.register()
        result = AppFunctions().add_quote(self.username, self.quote)
        self.assertTrue(result)

    def test_add_quote_fails_without_username(self):
        result = AppFunctions().add_quote("", self.quote)
        self.assertIsNone(result)

    def test_show_user_success(self):
        self.register()
        result = AppFunctions().show_user(self.username)
        self.assertTrue(result)

    def test_show_user_fail(self):
        result = AppFunctions().show_user(self.username)
        self.assertFalse(result)
