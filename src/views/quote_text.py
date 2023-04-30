import ttkbootstrap as ttk

class QuoteText(ttk.Frame):
    def __init__(self, parent, response_text, response_author, response_tags):
        super().__init__(master=parent)
        self.grid(column=1, row=0, rowspan=3, columnspan=1,
                  sticky="ns", padx=10, pady=20)
        self.rowconfigure(0, weight=1, uniform="b")
        self.rowconfigure(1, weight=2, uniform="b")
        self.rowconfigure(2, weight=2, uniform="b")
        self.rowconfigure(3, weight=2, uniform="b")
        self.rowconfigure(4, weight=2, uniform="b")
        self.canvas = ttk.Canvas(self, bg="#FFFFFF")
        self.canvas.grid(row=1, column=1, rowspan=2, sticky="nsew")
        self.content_frame = ttk.Frame(self.canvas)
        self.content_frame.bind("<Configure>", lambda event: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window(
            (0, 0), window=self.content_frame, anchor="nw")

        self.text_label = ttk.Label(
            self.content_frame,
            textvariable=response_text,
            anchor="center",
            justify="center",
            wraplength=350,
            width=23,
            font=("Comic Sans MS", 20)
        )

        self.text_label.pack()
        self.text_label.bind("<Button-4>", self._on_mousewheel)
        self.text_label.bind("<Button-5>", self._on_mousewheel)

        author_label = ttk.Label(
            self,
            textvariable=response_author,
            font="Calibri 20 bold",
        )
        author_label.grid(row=3, column=1)
        tag_label = ttk.Label(
            self,
            textvariable=response_tags,
        )
        tag_label.grid(row=4, column=1, sticky="n")
    
    def _on_mousewheel(self, event):
        if event.num == 4:
            direction = -1
        elif event.num == 5:
            direction = 1
        else:
            return
        self.canvas.yview_scroll(direction, "units")

