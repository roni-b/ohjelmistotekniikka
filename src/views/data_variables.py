import tkinter as tk

class Data:
    def __init__(self):
        self.response_text = tk.StringVar()
        self.response_author = tk.StringVar()
        self.response_tags = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.reg_or_log = tk.BooleanVar(value=False)
        self.user_content = tk.StringVar()
        self.search_var = tk.StringVar()
        self.hide_text = tk.StringVar(value="Hide quote")
        self.category = tk.StringVar(value="Select category")
        self.categories = tk.StringVar(value="All")
