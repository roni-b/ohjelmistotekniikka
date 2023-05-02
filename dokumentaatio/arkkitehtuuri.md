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
