import json
import requests
from model import db_models

class AppFunctions:
    """Luokka, jonka metodeja kutsutaan käyttöliittymäkoodista.
    """
    def __init__(self):
        pass

    @staticmethod
    def login(username, password):
        """Palauttaa tiedon kirjautumisen onnistumisesta/epäonnistumisesta.

        Args:
            username (string): Käyttäjän syöttämä tunnus
            password (string): Käyttäjän syöttämä salasana

        Returns:
            Tuple, jonka ensimmäinen arvo on True tai False.
            Toinen arvo merkkijono onnistuneesta tai
            epäonnistuneesta kirjautumisesta.
        """
        if db_models.login(username, password):
            return True, f"welcome {username}!"
        return False, "login failed"

    @staticmethod
    def register(username, password):
        """Tarkistaa tunnuksen ja salasanan pituuden ja
           rekisteröitymisen onnistumisen/epäonnistumisen
        Args:
            username (string): Käyttäjän syöttämä tunnus
            password (string): Käyttäjän syöttämä salasana

        Returns:
            Tuple, jonka ensimmäinen arvo on True tai False.
            Toinen arvo merkkijono onnistuneesta tai
            epäonnistuneesta rekisteröitymisestä.
        """
        if len(username) < 3 or len(password) < 3:
            return False
        if db_models.register(username, password):
            return True, "register successful"
        return False, "register failed"

    @staticmethod
    def get_api_response(api_url):
        """Hakee API-osoitteesta datan

        Args:
            api_url (string): API:n osoite

        Raises:
            ValueError("Connection timeout") Jos pyyntö on aikakatkaistu
            ValueError("Connection error") Jos yhteyttä ei voida muodostaa
            ValueError("HTTP error") Jos HTTP-pyyntöön vastataan esim. 404 statuskoodilla
            ValueError("JSONDecode error") Jos JSON-vastauksen muunto Python-objektiksi epäonnistuu

        Returns:
           response.json(): API:n vastaus JSON-muodossa
        """
        try:
            response = requests.get(api_url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout as exc:
            raise ValueError("Connection timeout") from exc
        except requests.exceptions.ConnectionError as exc:
            raise ValueError("Connection error") from exc
        except requests.exceptions.HTTPError as err:
            raise ValueError(f"{err}") from err
        except json.JSONDecodeError as err:
            raise ValueError(f"Error decoding JSON: {err}") from err

    def get_new_quote(self, category):
        """Määrittää API:n osoitteen valitun kategorian mukaan
        välittää osoitteen yllä olevalle metodille ja tarkistaa
        datan olemassaolon.

        Args:
            category (string): Käyttäjän valitsema kategoria

        Returns:
            Tuple: palauttaa API:n palauttaman datan tai virheilmoituksen.
        """
        if category in ('Select category', 'All'):
            api_url = 'https://api.quotable.io/quotes/random'
        else:
            api_url = f"https://api.quotable.io/quotes/random?tags={category.lower()}"
        try:
            data = self.get_api_response(api_url)
            content = data[0]["content"]
            author = data[0]["author"]
            tags = data[0]["tags"]
            if not all([content, author, tags]):
                return (True, "Some part of the response data is empty")
            return content, author, tags
        except ValueError as err:
            return (True, f"Error: {err}")
        except KeyError:
            return (True, "The response data is missing")
        except IndexError:
            return (True, "Index error while retrieving the data")

    @staticmethod
    def show_user(username):
        """Hakee käyttäjän oman sivun

        Args:
            username (string): Kirjautuneen käyttäjän tunnus

        Returns:
            Dictionary, jossa käyttäjän sisältö, virheen tapahtuessa False.
        """
        return db_models.show_user(username)

    @staticmethod
    def add_quote(username, quote):
        """Lisää uuden lainauksen

        Args:
            username: käyttäjätunnus
            quote: uusi lainaus

        Returns:
            True, jos lisäys onnistui, muuten None.
        """
        if not username:
            return None
        new = [quote[0], quote[1], quote[2]]
        return db_models.add_quote(username, new)

    def get_categories(self):
        """Hakee kategoriat

        Returns:
            Merkkijonon, jossa kategoriat tai True
            jos tapahtui virhe.
        """
        api_url = 'https://api.quotable.io/tags'
        parsed = ""
        try:
            data = self.get_api_response(api_url)
            for i in data:
                if i["quoteCount"] != 0:
                    parsed += i["name"]+" "
            return parsed
        except ValueError as err:
            return (
                True, f"An error occurred while retrieving the category data from the server: {err}"
                )
        except KeyError:
            return (True, "The categories data is missing")
