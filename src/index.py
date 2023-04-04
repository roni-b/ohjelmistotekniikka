import tkinter as tk
#import ttkbootstrap as ttk
from tkinter import ttk
from app_functions import test

class App(tk.Tk):
    def __init__(self):
        super().__init__()#themename="journal")
        self.title("")
        self.width = 800
        self.height = 800
        self.resizable(False, False)
        self.display_width = self.winfo_screenwidth()
        self.display_height = self.winfo_screenheight()
        self.left = int(self.display_width/2-self.width/2)
        self.top = int(self.display_height/2-self.height/2)
        self.geometry(f"{self.width}x{self.height}+{self.left}+{self.top}")
        self.bind("<Escape>", lambda event: self.quit())

        self.columnconfigure((0,1), weight=1, uniform="a")
        self.rowconfigure((0,1,2,3), weight=1, uniform="a")

        #data
        self.response_text = tk.StringVar(value="response from api")
        self.update_response_text()

        #widgets
        GetQuoteButton(self, self.response_text)
        QuoteText(self, self.response_text)
        #NewQuote(self, self.response_text)
        self.mainloop()

    def update_response_text(self):
        new_quote = test()
        representation = f"{new_quote[0]} {new_quote[1]}"
        self.response_text.set(representation)


class GetQuoteButton(ttk.Button):
    def __init__(self, parent, response_text):
        super().__init__(command=lambda: self.update_quote(), master=parent, text="Get Quote!")
        self.grid(column=1, row=2, rowspan=1, sticky="nsew")
        self.response_text = response_text
    
    def update_quote(self):
        new_quote = test()
        representation = f"{new_quote[0]} {new_quote[1]}"
        self.response_text.set(representation)

class QuoteText(ttk.Label):
    def __init__(self, parent, response_text):
        super().__init__(master=parent, text="test", font="Calibri 10", textvariable=response_text)
        self.grid(column=0, row=0, rowspan=1, columnspan=2, sticky="nsew")

class NewQuote(ttk.Frame):
    def __init__(self, parent, response_text):
        super().__init__(master=parent)
        self.grid(column=0, row=0, rowspan=2, columnspan=2, sticky="nsew")
        text = ttk.Label(self, text="", textvariable=response_text)
        text.grid(row=0, column=0)
        button = ttk.Button(self, text="Get Quote!")
        button.grid(row=3, column=1)








if __name__ == '__main__':
    App()
