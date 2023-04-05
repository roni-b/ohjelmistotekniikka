import db_models
import requests

class AppFunctions:
    def __init__(self):
        self.__users = "get all users"
        self.__quotes = "get all quotes"
    
    def login(self, username, password):
        pass

    def register(self, username, password):
        pass

    def get_new_quote(self):
        api_url = 'https://api.quotable.io/random'
        response = requests.get(api_url)
        if response.status_code == requests.codes.ok:
            data = response.json()
            content = data["content"]
            author = data["author"]
            tags = data["tags"]
            return content, author, tags
        else:
            print("Error:", response.status_code, response.text)


    def show_all_quotes(self):
        return self.__quotes
    
    def show_all_users(self):
        return self.__users

def test():
    api_url = 'https://api.quotable.io/random'
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        data = response.json()
        content = data["content"]
        author = data["author"]
        tags = data["tags"]
        return content, author, tags
    else:
        print("Error:", response.status_code, response.text)