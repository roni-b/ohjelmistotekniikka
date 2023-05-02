import ttkbootstrap as ttk

class LoginForm(ttk.Frame):
    """Luokka, joka toteuttaa kirjautumisnäkymän.
    Args:
        Perii ttk-ikkunan.
    """
    def __init__(self, parent, username, password, register_or_login):
        """Luokan konstruktori, joka asettaa parametrit ja kutsuu lopuksi näkymän
        luovaa metodia.

        Args:
            parent: Yliluokan self
            username: Käyttäjätunnus
            password: Salasana
            register_or_login: Kertoo totuusarvolla kumpi on kyseessä.
        """
        super().__init__(master=parent)
        self.grid(row=0, column=0, rowspan=1, columnspan=1,
                  sticky="nsew", padx=10, pady=10)

        self.app_instance = parent
        self.username = username
        self.password = password
        self.register_or_login = register_or_login

        for i in range(4):
            self.rowconfigure(i, weight=1, uniform="b")

        for i in range(3):
            self.columnconfigure(i, weight=1, uniform="b")

        self.create_widgets()

    def create_widgets(self):
        """Asettaa kirjautumislomakkeen näkyväksi.
        """
        self.label = ttk.Label(self, text="Login")
        self.label.grid(row=0, column=0, sticky="nw")

        self.username_label = ttk.Label(self, text="Username")
        self.username_entry = ttk.Entry(self, textvariable=self.username)
        self.username_label.grid(row=1, column=0, sticky="nsew")
        self.username_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

        self.password_label = ttk.Label(self, text="Password")
        self.password_entry = ttk.Entry(self, show="*", textvariable=self.password)
        self.password_label.grid(row=2, column=0, sticky="nsew")
        self.password_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

        self.checkbutton = ttk.Checkbutton(
            self, bootstyle="round-toggle", variable=self.register_or_login,text="Register")
        self.checkbutton.grid(row=3, column=0, sticky="w")
        self.submit_button = ttk.Button(
            # pylint: disable=W0108
            # lambda is necessary
            self,
            command=lambda: self.app_instance.login_form_submit_handler(),
            text="Login/register")
        self.submit_button.grid(row=3, column=1, columnspan=2, sticky="nsew")
