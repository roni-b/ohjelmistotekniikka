## Sovelluksen tarkoitus

Ideana on tehdä sovellus, joka näyttää erilaisia lyhyitä satunnaisia lainauksia/sitaatteja eri henkilöiltä. Lainaukset haetaan [Quotable API](https://github.com/lukePeavey/quotable) -palvelusta käyttäen Pythonin Requests -moduulia. Käyttäjä voi halutessaan tallentaa lainauksia tietokantaan, jolloin ne ovat aina saatavilla. Käyttäjä voi myös piilottaa näkyvistä sellaiset lainaukset mistä ei pidä. Sovellukseen on mahdollista rekisteröidä tunnus ja käyttäjälle näytetään oma näkymänsä lainauksista.

## Käyttäjät

Yksi käyttäjärooli, eli normaali käyttäjä.

## Perusversion tarjoama toiminnallisuus

**Ennen kirjautumista**
- Käyttäjä voi luoda käyttäjätunnuksen
  - Tunnus ja salasana oltava vähintään 3 merkkiä pitkä
- Käyttäjä voi kirjautua sovellukseen kirjautumislomakkeen avulla
- Sovellus tarkistaa, että tunnus ja salasana täsmäävät
  - Sovellus ilmoittaa kirjautumisen onnistumisesta

**Kirjautumisen jälkeen**

- Käyttäjä näkee tallennetut lainaukset ja painikkeen mistä saa haettua uuden lainauksen
- Käyttäjän klikatessa painiketta, uusi lainaus näytetään ja avautuu valikko
  - Valikossa toiminnot, jolla lainauksen saa tallennettua tietokantaan, piilotettua näkyvistä tai vaihdettua kategorian
- Käyttäjä voi järjestää ja hakea tallennettuja lainauksia hakutoiminnolla 

**Jatkokehitysideoita**

- Käyttäjätunnuksen poistaminen
- Tallennetun lainauksen poistaminen
- Tietyn tekijän lainausten hakeminen API:sta
  - Tai hakusanalla haku
