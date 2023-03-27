## Sovelluksen tarkoitus

Ideana on tehdä sovellus joka näyttää erilaisia lyhyitä satunnaisia lainauksia eri henkilöiltä. Lainaukset haetaan Quotable API -palvelusta käyttäen Pythonin Requests -moduulia. Käyttäjä voi halutessaan tallentaa lainauksia tietokantaan, jolloin ne ovat aina saatavilla (on myös mahdollista poistaa). Käyttäjä voi myös piilottaa näkyvistä sellaiset lainaukset mistä ei pidä. Sovellukseen on mahdollista rekisteröidä tunnus ja käyttäjälle näytetään oma näkymänsä lainauksista. 

## Käyttäjät

Yksi käyttäjärooli, eli normaali käyttäjä. Myöhemmin saatetaan lisätä pääkäyttäjä jos on tarvetta.

## Perusversion tarjoama toiminnallisuus

Ennen kirjautumista

- Käyttäjä voi luoda uniikin käyttäjätunnuksen
- Käyttäjä voi kirjautua sovellukseen kirjautumislomakkeen avulla
- Sovellus tarkistaa, että tunnus ja salasana täsmäävät

Kirjautumisen jälkeen

- Käyttäjä näkee tallennetut lainaukset ja painikkeen mistä saa haettua uuden lainauksen
- Uuden lainauksen mukana toiminto jolla sen saa tallennettua tietokantaan tai piilotettua näkyvistä
- Mahdollisuus kirjautua ulos

Jatkokehitysideoita

- Tietokannassa olevien lainausten järjestäminen jollain tavalla
- Hakutoiminto tietyn lainauksen tai sen tekijän etsimiseen
