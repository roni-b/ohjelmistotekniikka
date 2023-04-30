from tkinter import messagebox, font
import ttkbootstrap as ttk
from controller.app_functions import AppFunctions
from views.widgets import Widgets
from views.data_variables import Data
from config import TITLE, WIDTH, HEIGHT, RESIZABLE, FONT_FAMILY, FONT_SIZE, FONT_WEIGHT, COLUMNS, ROWS, ERROR_TITLE

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="vapor")
        self.title(TITLE)
        self.width = WIDTH
        self.height = HEIGHT
        self.resizable(*RESIZABLE)
        self.geometry(self._center_position(WIDTH, HEIGHT))
        self.bind("<Escape>", lambda event: self.quit())
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(family=FONT_FAMILY, size=FONT_SIZE, weight=FONT_WEIGHT)
        self.columnconfigure(COLUMNS, weight=1, uniform="a")
        self.rowconfigure(ROWS, weight=1, uniform="a")

        self.data = Data()

        self.widgets = Widgets(self, self.data)

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
        parsed_data = ""
        search_term = self.data.search_var.get().lower()
        for i in response["quotes"]:
            author = i['author'].lower()
            content = i['content'].lower()
            tags = str(i['tags'].lower()).strip(",")
            qid = i['id']
            if (search_term in author) or (search_term in content) or (search_term in str(qid)) or (search_term in tags):
                parsed_data += f"id:{qid}\ntags: {tags}\n{content}\n{author}\n\n"
        self.data.user_content.set(parsed_data)
   
    def search_handler(self, *args):
        self.sort_user_page()

    def get_categories(self):
        all = AppFunctions().get_categories()
        if all[0] == True:
            messagebox.showerror(title=ERROR_TITLE, message=all[1])
        else:
            self.data.categories.set(all)

if __name__ == '__main__':
    App()
