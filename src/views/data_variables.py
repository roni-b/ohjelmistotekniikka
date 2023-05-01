import tkinter as tk

class Response:
    def __init__(self):
        self.text = tk.StringVar()
        self.author = tk.StringVar()
        self.tags = tk.StringVar()

class User:
    def __init__(self):
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.content = tk.StringVar()

class OtherData:
    def __init__(self):
        self.search_var = tk.StringVar()
        self.hide_text = tk.StringVar(value="Hide quote")
        self.category = tk.StringVar(value="Select category")
        self.categories = tk.StringVar(value="All")
        self.register_or_login = tk.BooleanVar(value=False)
