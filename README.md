# Random Quote App
kuvaus 

[relase](https://github.com/roni-b/ohjelmistotekniikka/releases/tag/viikko5)

### Dokumentaatio

- [vaatimusmäärittely](https://github.com/roni-b/ohjelmistotekniikka/blob/main/dokumentaatio/vaatimusmaarittely.md)

- [tuntikirjanpito](https://github.com/roni-b/ohjelmistotekniikka/blob/main/dokumentaatio/tuntikirjanpito.md)

- [changelog](https://github.com/roni-b/ohjelmistotekniikka/blob/main/dokumentaatio/changelog.md)

- [arkkitehtuuri](https://github.com/roni-b/ohjelmistotekniikka/blob/main/dokumentaatio/arkkitehtuuri.md)

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

