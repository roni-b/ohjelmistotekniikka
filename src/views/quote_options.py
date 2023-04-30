import ttkbootstrap as ttk
from controller.app_functions import AppFunctions

class QuoteOptions(ttk.Frame):
    def __init__(self,
                parent,
                response_text,
                response_author,
                response_tags,
                text_widget,
                hide_text,
                username,
                category,
                categories):
        super().__init__(master=parent)
        self.app_instance = parent
        self.text_widget = text_widget
        self.username = username
        self.response_text = response_text
        self.response_author = response_author
        self.response_tags = response_tags
        self.hide_text = hide_text
        self.category = category
        self.categories = categories
        self.grid(column=1, row=2, padx=10, sticky="s")
        self.btn_frame = ttk.Frame(self)
        self.btn_frame.grid(column=1, row=2)
        self.btn_frame.columnconfigure(0, weight=1, uniform="b")
        self.btn_frame.columnconfigure(1, weight=1, uniform="b")
        self.btn_frame.columnconfigure(2, weight=2, uniform="b")
        self.button1 = ttk.Button(
            self.btn_frame, text="Save quote", command=self.save_quote)
        self.button1.grid(column=0, row=2, sticky="nsew")
        self.button2 = ttk.Button(
            self.btn_frame, textvariable=self.hide_text, command=self.show_hide)
        self.button2.grid(column=1, row=2, sticky="nsew")
        self.b_label = ttk.Label(self.btn_frame, style="primary.Inverse.TLabel")
        self.b_label.grid(column=2, row=2, sticky="nsew")
        combo = ttk.Combobox(self.b_label,
                            state="readonly",
                            textvariable=self.category,
                            style='info.TCombobox'
                            )
        self.app_instance.get_categories()
        combo['values'] = 'All ' + self.categories.get()
        #combo.bind('<<ComboboxSelected>>', lambda event: print(self.category.get()))
        combo.place(x=10, y=6)
    def show_hide(self):
        if self.hide_text.get() == "Hide quote":
            self.hide_text.set("Show quote")
            self.text_widget.grid_remove()
        else:
            self.text_widget.grid()
            self.hide_text.set("Hide quote")

    def save_quote(self):
        if self.username.get():
            AppFunctions().add_quote(self.username.get(), [
                self.response_text.get(), self.response_author.get(), self.response_tags.get()])
            self.app_instance.refresh_user_page()
