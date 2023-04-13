## Sovelluksen tarkoitus

Ideana on tehdä sovellus, joka näyttää erilaisia lyhyitä satunnaisia lainauksia eri henkilöiltä. Lainaukset haetaan [Quotable API](https://github.com/lukePeavey/quotable) -palvelusta käyttäen Pythonin Requests -moduulia. Käyttäjä voi halutessaan tallentaa lainauksia tietokantaan, jolloin ne ovat aina saatavilla (on myös mahdollista poistaa). Käyttäjä voi myös piilottaa näkyvistä sellaiset lainaukset mistä ei pidä. Sovellukseen on mahdollista rekisteröidä tunnus ja käyttäjälle näytetään oma näkymänsä lainauksista.

## Käyttäjät

Yksi käyttäjärooli, eli normaali käyttäjä. Myöhemmin saatetaan lisätä pääkäyttäjä jos on tarvetta.

## Perusversion tarjoama toiminnallisuus

Ennen kirjautumista
- :heavy_check_mark: Käyttäjä voi luoda uniikin käyttäjätunnuksen
- :heavy_check_mark: Käyttäjä voi kirjautua sovellukseen kirjautumislomakkeen avulla
- :heavy_check_mark: Sovellus tarkistaa, että tunnus ja salasana täsmäävät

Kirjautumisen jälkeen

- :heavy_check_mark: Käyttäjä näkee tallennetut lainaukset ja painikkeen mistä saa haettua uuden lainauksen
- :heavy_check_mark: Uuden lainauksen mukana toiminto jolla sen saa tallennettua tietokantaan tai piilotettua näkyvistä
- :heavy_check_mark: Mahdollisuus kirjautua ulos

Jatkokehitysideoita

- :x: Lainausten järjestäminen jollain tavalla
- :x: Hakutoiminto tietyn lainauksen tai sen tekijän etsimiseen
