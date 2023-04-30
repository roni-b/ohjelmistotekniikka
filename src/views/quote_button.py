import ttkbootstrap as ttk
from tkinter import messagebox
from controller.app_functions import AppFunctions

class GetQuoteButton(ttk.Button):
    def __init__(self, parent, response_text, response_author, response_tags, options, text, category):
        # pylint: disable=W0108
        # lambda is necessary
        super().__init__(command=lambda: self.update_quote(),
                         master=parent, text="Get random quote")
        self.options = options
        self.text = text
        self.category = category
        self.grid(column=1, row=3, rowspan=1, sticky="nsew", padx=10, pady=10)
        self.content = response_text
        self.author = response_author
        self.tags = response_tags

    def update_quote(self):
        new_quote = AppFunctions().get_new_quote(self.category.get())
        if new_quote[0] == True:
            messagebox.showerror(title="Error", message=new_quote[1])
        else:
            self.content.set(new_quote[0])
            self.author.set(new_quote[1])
            bad_chars = ['"', "'", '{', '}', '[', ']']
            filtered_tags = [tag for tag in new_quote[2] if tag not in bad_chars]
            self.tags.set(', '.join(filtered_tags))
            self.text.grid()
            self.options.grid()
