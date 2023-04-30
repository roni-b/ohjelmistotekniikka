import ttkbootstrap as ttk

class UserPage(ttk.Frame):
    def __init__(self, parent, content, search_var):
        super().__init__(master=parent)
        self.app_instance = parent
        self.grid(row=0, column=0, rowspan=4, columnspan=1,
                  sticky="nsew", padx=10, pady=10)
        self.rowconfigure(0, weight=1, uniform="b")
        self.rowconfigure(1, weight=10, uniform="b")
        self.columnconfigure(0, weight=1, uniform="b")
        self.label = ttk.Label(self, text="User page")
        self.label.grid(row=0, column=0, sticky="nw")
        self.logout_button = ttk.Button(
            self, text="Logout", command=lambda: self.app_instance.logout_function())
        self.logout_button.grid(row=0, column=0, sticky="ne")

        self.search_entry = ttk.Entry(self, textvariable=search_var)
        self.search_entry.grid(column=0, row=0, sticky="n")
        self.search_entry.insert(0, "Search quote")
        self.search_entry.bind("<FocusIn>", self.on_entry_focusin)

        self.canvas = ttk.Canvas(self, bg="#FFFFFF")
        self.canvas.grid(row=1, column=0, sticky="nsew")
        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=1, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.content_frame = ttk.Frame(self.canvas)
        self.content_frame.bind("<Configure>", lambda event: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window(
            (0, 0), window=self.content_frame, anchor="nw")
        self.text_label = ttk.Label(
            self.content_frame,
            textvariable=content,
            anchor="center",
            justify="center",
            wraplength=400,
            font=("Comic Sans MS", 15),
        )
        self.text_label.pack(fill="both", expand=True)
        self.text_label.bind("<Button-4>", self._on_mousewheel)
        self.text_label.bind("<Button-5>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        if event.num == 4:
            direction = -1
        elif event.num == 5:
            direction = 1
        else:
            return
        self.canvas.yview_scroll(direction, "units")
    
    def on_entry_focusin(self, event):
        if self.search_entry.get() == "Search quote":
            self.search_entry.delete(0, ttk.END)
