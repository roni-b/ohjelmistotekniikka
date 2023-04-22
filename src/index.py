import tkinter as tk
from tkinter import messagebox, font
import ttkbootstrap as ttk
from app_functions import AppFunctions

class Data:
    def __init__(self):
        self.response_text = tk.StringVar()
        self.response_author = tk.StringVar()
        self.response_tags = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.reg_or_log = tk.BooleanVar(value=False)
        self.user_content = tk.StringVar()
        self.search_var = tk.StringVar()
        self.hide_text = tk.StringVar(value="Hide quote")
        self.category = tk.StringVar(value="Select category")
        self.categories = tk.StringVar(value="All")

class Widgets:
    def __init__(self, master, data):
        self.quote_text = QuoteText(
            master,
            data.response_text,
            data.response_author,
            data.response_tags
        )
        self.quote_options = QuoteOptions(
            master,
            data.response_text,
            data.response_author,
            data.response_tags,
            self.quote_text,
            data.hide_text,
            data.username,
            data.category,
            data.categories
        )
        self.get_quote_button = GetQuoteButton(
            master,
            data.response_text,
            data.response_author,
            data.response_tags,
            self.quote_options,
            self.quote_text,
            data.category
        )
        self.user_page = UserPage(
            master,
            data.user_content,
            data.search_var
        )
        self.login_form = LoginForm(
            master, data.username,
            data.password,
            data.reg_or_log,
            self.user_page,
            data.user_content
        )
        self.quote_text.grid_remove()
        self.quote_options.grid_remove()
        self.user_page.grid_remove()

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="vapor")
        self.title("")
        self.width = 1000
        self.height = 800
        self.resizable(False, False)
        self.geometry(self._center_position(self.width, self.height))
        self.bind("<Escape>", lambda event: self.quit())
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(family="Comic Sans MS", size=15, weight=font.BOLD)
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")
        # data
        self.data = Data()

        # widgets
        self.widgets = Widgets(self, self.data)

        #tracing
        self.data.search_var.trace("w", self.search_handler)

        self.mainloop()

    def _center_position(self, width, height):
        display_width = self.winfo_screenwidth()
        display_height = self.winfo_screenheight()
        left = int(display_width / 2 - width / 2)
        top = int(display_height / 2 - height / 2)
        return f"{width}x{height}+{left}+{top}"

    def logout_function(self):
        self.widgets.user_page.grid_remove()
        self.widgets.login_form.grid()
        self.data.username.set(value="")
        self.data.password.set(value="")

    def refresh_user_page(self):
        response = AppFunctions().show_user(self.data.username.get())
        parsed = ""
        for i in response["quotes"]:
            tags = str(i['tags']).strip(",")
            parsed += f"id:{i['id']}\ntags: {tags}\n{i['content']}\n{i['author']}\n\n"
        self.data.user_content.set(parsed)

    def sort_user_page(self):
        response = AppFunctions().show_user(self.data.username.get())
        parsed = ""
        search_term = self.data.search_var.get().lower()
        for i in response["quotes"]:
            author = i['author'].lower()
            content = i['content'].lower()
            tags = str(i['tags'].lower()).strip(",")
            qid = i['id']
            if (search_term in author) or (search_term in content) or (search_term in str(qid)) or (search_term in tags):
                parsed += f"id:{qid}\ntags: {tags}\n{content}\n{author}\n\n"
        self.data.user_content.set(parsed)
   
    def search_handler(self, *args):
        self.sort_user_page()

    def get_categories(self):
        all = AppFunctions().get_categories()
        if all[0] == True:
            messagebox.showerror(title="Error", message=all[1])
        else:
            self.data.categories.set(all)

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

class QuoteText(tk.Frame):
    def __init__(self, parent, response_text, response_author, response_tags):
        super().__init__(master=parent)
        self.grid(column=1, row=0, rowspan=3, columnspan=1,
                  sticky="ns", padx=10, pady=20)
        self.rowconfigure(0, weight=1, uniform="b")
        self.rowconfigure(1, weight=2, uniform="b")
        self.rowconfigure(2, weight=2, uniform="b")
        self.rowconfigure(3, weight=2, uniform="b")
        self.rowconfigure(4, weight=2, uniform="b")
        self.canvas = tk.Canvas(self, bg="#FFFFFF")
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


class QuoteOptions(tk.Frame):
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

        self.canvas = tk.Canvas(self, bg="#FFFFFF")
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
            self.search_entry.delete(0, tk.END)

if __name__ == '__main__':
    App()
