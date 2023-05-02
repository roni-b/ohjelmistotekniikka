## Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa MVC-arkkitehtuuria, jossa käyttöliittymä on eriytetty sovelluslogiikasta. 

Hakemistossa ```model``` sijaitsee tietokantakuvaus ja funktiot tietokannan käyttämiseen.

Hakemistossa ```controller``` sijaitsee sovelluslogiikka.

Käyttöliittymäkoodi sijaitsee ```views``` hakemistossa ja se on jaoteltu useampaan näkymätiedostoon. Lisäksi siellä on ```data_variables``` tiedosto, joka sisältää kaikki Tkinter muuttujat, mitä sovelluksessa käytetään. Tiedostosta ```widgets``` kutsutaan näkymätiedostojen luokkia.

![Pakkauskaavio](https://user-images.githubusercontent.com/104189902/235663064-0ad23c1c-8805-476d-84a1-2e105abb52c3.png)

Hakemistorakenne pakkauskaaviona, jossa riippuvuudet on merkitty katkoviivalla.

## Sovelluslogiikka

Ohjelman sovelluslogiikka on luokassa ```AppFunctions``` ja se sisältää kaikki käyttöliittymän tarvitsemat metodit. Luokan metodit käyttävät tietojen tallentamiseen ja hakemiseen ```db_models``` tiedoston funktioita. 



## Sekvenssikaaviot 

Alla on kuvattuna sovelluksen päätoiminnallisuudet sekvenssikaavioina:

![Screenshot from 2023-04-21 16-21-10](https://user-images.githubusercontent.com/104189902/233646579-f17151e4-4aa9-46e4-9c12-51a49357bac5.png)

Kun käyttäjä klikkaa uuden lainauksen hakupainikkeesta, käyttöliittymäkoodi kutsuu sovelluslogiikasta uuden lainauksen hakumetodia `get_new_quote` . Sitten `get_api_response` metodi hakee kyseisestä rajapinnasta uuden lainauksen ja palauttaa saamansa datan `get_new_quote` metodille JSON-muodossa, joka vuorostaan palauttaa sen käyttöliittymälle tuplena: *content, author, tags* . Saatuaan datan, käyttöliittymä asettaa ne omiin muuttujiinsa ja määrittää `.grid` komennoilla uuden lainauksen ja sen toiminnot näkyviksi.

![Screenshot from 2023-04-21 17-28-39](https://user-images.githubusercontent.com/104189902/233661967-29023478-63c9-4e0d-8bfa-687ec037666c.png)

Kirjauduttaessa kutsutaan sovelluslogiikan metodia login, jolle annetaan parametreiksi tunnus ja salasana. Sovelluslogiikka välittää tunnuksen ja salasanan tietokantaoperaatiolle login, joka tarkistaa onko tunnus olemassa ja salasana oikein. Jos ne ovat oikein, funktio palauttaa True ja sovelluslogiikka palauttaa käyttöliittymälle True sekä viestin onnistuneesta kirjautumisesta. Käyttöliittymä poistaa kirjautumislomakkeen näkyvistä ja sen tilalle tulee käyttäjän sivu. Lisäksi käyttäjän sivu uudelleenladataan, jolla varmistetaan sisällön ajantasaisuus. Lopuksi käyttäjälle näytetään viesti onnistuneesta kirjautumisesta.
