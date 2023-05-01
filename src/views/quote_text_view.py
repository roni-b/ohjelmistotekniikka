import ttkbootstrap as ttk
from utils import create_content_frame

class QuoteText(ttk.Frame):
    def __init__(self, parent, response_text, response_author, response_tags):
        super().__init__(master=parent)
        self.grid(column=1, row=0, rowspan=3, columnspan=1,
                  sticky="ns", padx=10, pady=20)
        self.rowconfigure(0, weight=1, uniform="b")
        for i in range(1, 5):
            self.rowconfigure(i, weight=2, uniform="b")

        self.canvas = ttk.Canvas(self, bg="#FFFFFF")
        self.canvas.grid(row=1, column=1, rowspan=2, sticky="nsew")
        self.content_frame = create_content_frame(self.canvas)

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
        self.text_label.bind(
            "<Button-4>",
            lambda event: parent.on_mousewheel(event, self.text_label)
        )
        self.text_label.bind(
            "<Button-5>",
            lambda event: parent.on_mousewheel(event, self.text_label)
        )

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
