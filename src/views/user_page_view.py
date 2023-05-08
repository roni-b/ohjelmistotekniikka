import ttkbootstrap as ttk
from .utils import create_content_frame

class UserPage(ttk.Frame):
    """Luokka, joka toteuttaa käyttäjän sivun.

    Args:
        Perii ttk-ikkunan.
    """
    def __init__(self, parent, content, search_var):
        """Luokan konstruktori, joka asettaa rivit ja sarakkeet
        ja osan toiminnoista. Kutsuu lopuksi metodia joka toteuttaa
        sisällön näyttämisen.

        Args:
            parent: Yliluokan self
            content: Käyttäjän tallentamat lainaukset
            search_var: Sisältää nykyisen hakutermin
        """
        super().__init__(master=parent)
        self.app_instance = parent
        self.grid(row=0, column=0, rowspan=4, columnspan=1,
                  sticky="nsew", padx=10, pady=10)
        self.rowconfigure(0, weight=1, uniform="b")
        self.rowconfigure(1, weight=10, uniform="b")
        self.columnconfigure(0, weight=1, uniform="b")

        self.label = ttk.Label(self, text="User page")
        self.label.grid(sticky="nw")
        # pylint: disable=W0108
        # lambda is necessary
        self.logout_button = ttk.Button(
            self, text="Logout", command=lambda: self.app_instance.logout_function())
        self.logout_button.grid(row=0, column=0, sticky="ne")
        self.search_and_scroll(content, search_var)

    def search_and_scroll(self, content, search_var):
        """Asettaa hakupalkin ja käyttäjän lainaukset sekä toteuttaa skrollauksen.

        Args:
            content (_type_): _description_
            search_var (_type_): _description_
        """
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

        self.content_frame = create_content_frame(self.canvas)

        self.text_label = ttk.Label(
            self.content_frame,
            textvariable=content,
            anchor="center",
            justify="center",
            wraplength=400,
            font=("Comic Sans MS", 15),
        )
        self.text_label.pack(fill="both", expand=True)
        self.text_label.bind(
            "<Button-4>",
            lambda event: self.app_instance.on_mousewheel(event, self.canvas)
        )
        self.text_label.bind(
            "<Button-5>",
            lambda event: self.app_instance.on_mousewheel(event, self.canvas)
        )

    # pylint: disable=W0613
    # argument event is necessary
    def on_entry_focusin(self, event):
        """Poistaa hakupalkkia klikatessa alkutekstin

        Args:
            event: Sisältää tapahtuman parametrit
        """
        if self.search_entry.get() == "Search quote":
            self.search_entry.delete(0, ttk.END)
