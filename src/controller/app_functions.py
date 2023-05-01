import json
import requests
from model import db_models

class AppFunctions:
    def __init__(self):
        pass

    @staticmethod
    def login(username, password):
        if db_models.login(username, password):
            return True, f"welcome {username}!"
        return False, "login failed"

    @staticmethod
    def register(username, password):
        if len(username) < 3 or len(password) < 3:
            return False
        if db_models.register(username, password):
            return True, "register successful"
        return False, "register failed"

    @staticmethod
    def get_api_response(api_url):
        try:
            response = requests.get(api_url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout as exc:
            raise ValueError("Connection timeout") from exc
        except requests.exceptions.ConnectionError as exc:
            raise ValueError("Connection error") from exc
        except requests.exceptions.HTTPError as err:
            raise ValueError(f"{err}") from err
        except json.JSONDecodeError as err:
            raise ValueError(f"Error decoding JSON: {err}") from err

    def get_new_quote(self, category):
        if category in ('Select category', 'All'):
            api_url = 'https://api.quotable.io/quotes/random'
        else:
            api_url = f"https://api.quotable.io/quotes/random?tags={category.lower()}"
        try:
            data = self.get_api_response(api_url)
            content = data[0]["content"]
            author = data[0]["author"]
            tags = data[0]["tags"]
            if not all([content, author, tags]):
                return (True, "Some part of the response data is empty")
            return content, author, tags
        except ValueError as err:
            return (True, f"Error: {err}")
        except KeyError:
            return (True, "The response data is missing")
        except IndexError:
            return (True, "Index error while retrieving the data")

    @staticmethod
    def show_user(username):
        return db_models.show_user(username)

    @staticmethod
    def add_quote(username, quote):
        if not username:
            return None
        new = [quote[0], quote[1], quote[2]]
        return db_models.add_quote(username, new)

    def get_categories(self):
        api_url = 'https://api.quotable.io/tags'
        parsed = ""
        try:
            data = self.get_api_response(api_url)
            for i in data:
                if i["quoteCount"] != 0:
                    parsed += i["name"]+" "
            return parsed
        except ValueError as err:
            return (
                True, f"An error occurred while retrieving the category data from the server: {err}"
                )
        except KeyError:
            return (True, "The categories data is missing")
