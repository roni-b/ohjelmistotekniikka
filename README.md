# Random Quote App
Sovelluksen idea on näyttää lyhyitä satunnaisia lainauksia eri henkilöiltä, joita rekisteröitynyt käyttäjä voi tallentaa tietokantaan. Sovellus on Ohjelmistotekniikka-kurssin harjoitustyö.

[Relaset](https://github.com/roni-b/ohjelmistotekniikka/releases)

### Dokumentaatio

- [vaatimusmäärittely](https://github.com/roni-b/ohjelmistotekniikka/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [tuntikirjanpito](https://github.com/roni-b/ohjelmistotekniikka/blob/main/dokumentaatio/tuntikirjanpito.md)
- [changelog](https://github.com/roni-b/ohjelmistotekniikka/blob/main/dokumentaatio/changelog.md)
- [arkkitehtuuri](https://github.com/roni-b/ohjelmistotekniikka/blob/main/dokumentaatio/arkkitehtuuri.md)
- [käyttöohje](https://github.com/roni-b/ohjelmistotekniikka/blob/main/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)
- [testausdokumentti](https://github.com/roni-b/ohjelmistotekniikka/blob/main/dokumentaatio/testaus.md)

### Ohjelman ajo Docker-konttina

`xhost + && docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix roni120/ot-harjoitus "$@"`

### Asennus

Asenna riippuvuudet
```bash
poetry install
```
Alusta tietokanta
```bash
poetry run invoke build
```
Käynnistä sovellus
```bash
poetry run invoke start
```
*Sovelluksen toiminta on testattu Pythonin versiolla 3.11.2 ja Poetryn versiolla 1.4.1*
### Muut komennot
Luo testikattavuusraportti *htmlcov*-hakemistoon
```bash
poetry run invoke coverage-report
```
Aja testit
```bash
poetry run invoke test
```
Pylint tarkistukset komennolla
```bash
poetry run invoke lint
```

