# Testausdokumentti

Ohjelman testaus on suoritettu unittest yksikkö- ja integraatiotesteillä. Järjestelmätestaus on suoritettu manuaalisesti. 

### Sovelluslogiikka

Testiluokka `TestAppFunctions` testaa sovelluslogiikasta vastaavaa `AppFunctions`-luokkaa. Testit on toteutettu siten, että `AppFunctions`-luokan metodeja kutsutaan testien aluksi määritetyillä parametreilla. `AppFunctions` kutsuu normaalisti `db_models` tiedoston tietokantafunktioita ja tallentaa siten tietokantaan. Ennen testejä tietokannasta poistetaan testikäyttäjä- ja lainaus.

Lainausten haun integraatiotestauksessa on käytetty unittest.mock-kirjaston patch-metodia, jolla on asetettu sivuvaikutuksia requests.get-pyynnöille ja muokattu API:n palauttamaa dataa.

### Testauskattavuus

Testien haarautumakattavuus on 96%.

![Testikattavuus](https://github.com/roni-b/ohjelmistotekniikka/assets/104189902/e514b97f-a649-464f-a90f-2ab8e2cedc1e)
