from tkinter import messagebox, font
import ttkbootstrap as ttk
from controller.app_functions import AppFunctions
from views.widgets import Widgets
from views.data_variables import User, Response, OtherData

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
        self.default_font.configure(family="Comic Sans MS", size=15, weight="bold")
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")

        self.user_data = User()
        self.response_data = Response()
        self.other_data = OtherData()

        self.widgets = Widgets(self, self.user_data, self.response_data, self.other_data)

        self.other_data.search_var.trace("w", self.search_handler)

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
        self.user_data.username.set(value="")
        self.user_data.password.set(value="")

    def refresh_user_page(self):
        response = AppFunctions().show_user(self.user_data.username.get())
        parsed = ""
        for i in response["quotes"]:
            tags = str(i['tags']).strip(",")
            parsed += f"id:{i['id']}\ntags: {tags}\n{i['content']}\n{i['author']}\n\n"
        self.user_data.content.set(parsed)

    def sort_user_page(self):
        response = AppFunctions().show_user(self.user_data.username.get())
        parsed_data = ""
        search_term = self.other_data.search_var.get().lower()
        for i in response["quotes"]:
            author = i['author'].lower()
            content = i['content'].lower()
            tags = str(i['tags'].lower()).strip(",")
            qid = i['id']
            if (search_term in author or
                search_term in content or
                search_term in str(qid) or
                search_term in tags):
                parsed_data += f"id:{qid}\ntags: {tags}\n{content}\n{author}\n\n"
        self.user_data.content.set(parsed_data)
    #pylint: disable=W0613
    #parameter *args is necessary
    def search_handler(self, *args):
        self.sort_user_page()

    def get_categories(self):
        all_categories = AppFunctions().get_categories()
        if all_categories[0] is True:
            messagebox.showerror(title="Error", message=all_categories[1])
        else:
            self.other_data.categories.set(all_categories)

    def update_quote(self):
        new_quote = AppFunctions().get_new_quote(self.other_data.category.get())
        if new_quote[0] is True:
            messagebox.showerror(title="Error", message=new_quote[1])
        else:
            self.response_data.text.set(new_quote[0])
            self.response_data.author.set(new_quote[1])
            unwanted_characters = ['"', "'", '{', '}', '[', ']']
            filtered_tags = [tag for tag in new_quote[2] if tag not in unwanted_characters]
            self.response_data.tags.set(', '.join(filtered_tags))
            self.widgets.quote_text.grid()
            self.widgets.quote_options.grid()

    def save_quote(self):
        if self.user_data.username.get():
            AppFunctions().add_quote(
                self.user_data.username.get(),
                [self.response_data.text.get(),
                self.response_data.author.get(),
                self.response_data.tags.get()]
            )
            self.refresh_user_page()

    def show_hide(self):
        if self.other_data.hide_text.get() == "Hide quote":
            self.other_data.hide_text.set("Show quote")
            self.widgets.quote_text.grid_remove()
        else:
            self.widgets.quote_text.grid()
            self.other_data.hide_text.set("Hide quote")

    def login_form_submit_handler(self):
        if len(self.user_data.username.get()) >= 3 and len(self.user_data.password.get()) >= 3:
            if self.other_data.register_or_login.get():
                # register
                response = AppFunctions().register(
                    self.user_data.username.get(),
                    self.user_data.password.get()
                )
                if response[0]:
                    self.widgets.login_form.grid_remove()
                    self.refresh_user_page()
                    self.widgets.user_page.grid()
                messagebox.showinfo(title="Note", message=response[1])
            else:
                # login
                response = AppFunctions().login(
                    self.user_data.username.get(),
                    self.user_data.password.get()
                )
                if response[0]:
                    self.widgets.login_form.grid_remove()
                    self.refresh_user_page()
                    self.widgets.user_page.grid()
                messagebox.showinfo(title="Note", message=response[1])
        else:
            messagebox.showinfo(
                title="Note",
                message="Length of the username and the password must be at least 3 characters")

    @staticmethod
    def on_mousewheel(event, canvas):
        if event.num == 4:
            direction = -1
        elif event.num == 5:
            direction = 1
        else:
            return
        canvas.yview_scroll(direction, "units")

if __name__ == '__main__':
    App()
