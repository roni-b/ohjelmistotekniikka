import json
import requests
import db_models

class AppFunctions:
    def __init__(self):
        pass

    def login(self, username, password):
        if db_models.login(username, password):
            return True, f"welcome {username}!"
        return False, "login failed"

    def register(self, username, password):
        if len(username) < 3 or len(password) < 3:
            return False
        if db_models.register(username, password):
            return True, "register successful"
        return False, "register failed"

    def get_api_response(self, api_url):
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

    def get_new_quote(self):
        api_url = 'https://api.quotable.io/random'
        try:
            data = self.get_api_response(api_url)
            content = data["content"]
            author = data["author"]
            tags = data["tags"]
            if not all([content, author, tags]):
                return (True, "Some part of the response data is empty")
            return content, author, tags
        except ValueError as err:
            return (True, f"Error: {err}")
        except KeyError:
            return (True, "The response data is missing")

    def show_user(self, username):
        return db_models.show_user(username)

    def add_quote(self, username, quote):
        print(quote)
        if not username:
            return None
        bad_chars = ['"', "'", '(', ')']
        filtered = ''.join(
            map(lambda x: x if x not in bad_chars else '', quote[2]))
        new = [quote[0], quote[1], filtered]
        return db_models.add_quote(username, new)
