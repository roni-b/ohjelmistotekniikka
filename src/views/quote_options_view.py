import ttkbootstrap as ttk

class QuoteOptions(ttk.Frame):
    def __init__(self, parent, hide_text, category, categories):
        super().__init__(master=parent)
        self.app_instance = parent
        self.hide_text = hide_text
        self.category = category
        self.categories = categories

        self.grid(column=1, row=2, padx=10, sticky="s")

        self.btn_frame = ttk.Frame(self)
        self.btn_frame.grid(column=1, row=2)
        for i in range(3):
            self.btn_frame.columnconfigure(i, weight=1, uniform="b")

        self.button1 = ttk.Button(
            self.btn_frame, text="Save quote", command=self.app_instance.save_quote)
        self.button1.grid(column=0, row=2, sticky="nsew")
        self.button2 = ttk.Button(
            self.btn_frame, textvariable=self.hide_text, command=self.app_instance.show_hide)
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
        combo.place(x=10, y=6)
