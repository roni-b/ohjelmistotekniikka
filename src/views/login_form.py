import ttkbootstrap as ttk
from controller.app_functions import AppFunctions
from tkinter import messagebox

class LoginForm(ttk.Frame):
    def __init__(self, parent, username, password, reg_or_log, user_page, content):
        super().__init__(master=parent)
        self.app_instance = parent
        self.username = username
        self.password = password
        self.reg_or_log = reg_or_log
        self.user_page = user_page
        self.user_content = content
        self.grid(row=0, column=0, rowspan=1, columnspan=1,
                  sticky="nsew", padx=10, pady=10)
        self.rowconfigure(0, weight=1, uniform="b")
        self.rowconfigure(1, weight=1, uniform="b")
        self.rowconfigure(2, weight=1, uniform="b")
        self.rowconfigure(3, weight=1, uniform="b")
        self.columnconfigure(0, weight=1, uniform="b")
        self.columnconfigure(1, weight=1, uniform="b")
        self.columnconfigure(2, weight=1, uniform="b")
        self.label = ttk.Label(self, text="Login")
        self.label.grid(row=0, column=0, sticky="nw")

        self.username_label = ttk.Label(self, text="Username")
        self.username_entry = ttk.Entry(self, textvariable=username)
        self.username_label.grid(row=1, column=0, sticky="nsew")
        self.username_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

        self.password_label = ttk.Label(self, text="Password")
        self.password_entry = ttk.Entry(self, show="*", textvariable=password)
        self.password_label.grid(row=2, column=0, sticky="nsew")
        self.password_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

        self.checkbutton = ttk.Checkbutton(
            self, bootstyle="round-toggle", variable=reg_or_log)
        self.checkbutton.grid(row=3, column=0, sticky="w")
        self.label_register = ttk.Label(self, text="Register")
        self.label_register.grid(row=3, column=0)
        self.submit_button = ttk.Button(
            # pylint: disable=W0108
            # lambda is necessary
            self, command=lambda: self.submit(), text="Login/register")
        self.submit_button.grid(row=3, column=1, columnspan=2, sticky="nsew")

    def submit(self):
        if len(self.username.get()) >= 3 and len(self.password.get()) >= 3:
            if self.reg_or_log.get():
                # register
                response = AppFunctions().register(self.username.get(), self.password.get())
                if response[0]:
                    self.grid_remove()
                    self.user_page.grid()
                messagebox.showinfo(title="Note", message=response[1])
            else:
                # login
                response = AppFunctions().login(self.username.get(), self.password.get())
                if response[0]:
                    self.grid_remove()
                    self.app_instance.refresh_user_page()
                    self.user_page.grid()
                messagebox.showinfo(title="Note", message=response[1])
        else:
            messagebox.showinfo(
                title="Note",
                message="Length of the username and the password must be at least 3 characters")
