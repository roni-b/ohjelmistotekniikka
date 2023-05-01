from login_form_view import LoginForm
from quote_button_view import GetQuoteButton
from quote_options_view import QuoteOptions
from quote_text_view import QuoteText
from user_page_view import UserPage

class Widgets:
    def __init__(self, master, user_data, response_data, other_data):
        self.quote_text = QuoteText(
            master,
            response_data.text,
            response_data.author,
            response_data.tags
        )
        self.quote_options = QuoteOptions(
            master,
            other_data.hide_text,
            other_data.category,
            other_data.categories
        )
        self.get_quote_button = GetQuoteButton(
            master,
        )
        self.user_page = UserPage(
            master,
            user_data.content,
            other_data.search_var
        )
        self.login_form = LoginForm(
            master,
            user_data.username,
            user_data.password,
            other_data.register_or_login
        )
        self.quote_text.grid_remove()
        self.quote_options.grid_remove()
        self.user_page.grid_remove()
