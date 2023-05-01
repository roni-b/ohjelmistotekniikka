import ttkbootstrap as ttk

class GetQuoteButton(ttk.Button):
    def __init__(self, parent):
        self.app_instance = parent
        # pylint: disable=W0108
        # lambda is necessary
        super().__init__(
            command=lambda: self.app_instance.update_quote(),
            master=parent,
            text="Get random quote"
        )
        self.grid(column=1, row=3, rowspan=1, sticky="nsew", padx=10, pady=10)
