import tkinter as tk
from controller.app_functions import AppFunctions
import data_variables as data
from login_form import LoginForm
from quote_button import GetQuoteButton
from quote_options import QuoteOptions
from quote_text import QuoteText
from user_page import UserPage

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
            master,
            data.username,
            data.password,
            data.reg_or_log,
            self.user_page,
            data.user_content
        )
        self.quote_text.grid_remove()
        self.quote_options.grid_remove()
        self.user_page.grid_remove()
