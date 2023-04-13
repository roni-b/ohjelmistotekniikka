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

    def get_new_quote(self):
        api_url = 'https://api.quotable.io/random'
        try:
            response = requests.get(api_url, timeout=5)
            response.raise_for_status()
            data = response.json()
            content = data["content"]
            author = data["author"]
            tags = data["tags"]
            if not all([content, author, tags]):
                return "KeyError: Some part of the data is empty"
            return content, author, tags
        except requests.exceptions.Timeout:
            return "Error: Connection timeout"
        except requests.exceptions.ConnectionError:
            return "Error: Connection error"
        except requests.exceptions.HTTPError as err:
            return f"Error: {err}"
        except json.JSONDecodeError as err:
            return f"Error decoding JSON: {err}"
        except KeyError:
            return "KeyError: Some part of the data is missing"

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
    