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
        if db_models.register(username, password):
            return True, "register successful"
        return False, "register failed"

    def get_new_quote(self):
        # pylint: disable=E1101
        # requests.codes.ok gives an nonexistent menber error but that .ok member exists
        api_url = 'https://api.quotable.io/random'
        response = requests.get(api_url, timeout=5)
        if response.status_code == requests.codes.ok:
            data = response.json()
            content = data["content"]
            author = data["author"]
            tags = data["tags"]
            return content, author, tags
        return "Error:", response.status_code, response.text

    def show_user(self, username):
        return db_models.show_user(username)

    def add_quote(self, username, quote):
        if not username:
            return None
        bad_chars = ['"', "'", '(', ')']
        filtered = ''.join(
            map(lambda x: x if x not in bad_chars else '', quote[2]))
        new = [quote[0], quote[1], filtered]
        return db_models.add_quote(username, new)
    