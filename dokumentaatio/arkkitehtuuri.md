## Sovelluksen rakenne

![Kuvaus tietorakenteesta](https://user-images.githubusercontent.com/104189902/232098366-10bafba8-1d7a-40ca-b17e-573a0743ea8a.png)

Luokat User ja Quote määrittelevät db_functions tiedostossa sovelluksen tietokantataulut

![Screenshot from 2023-04-14 19-25-54](https://user-images.githubusercontent.com/104189902/232102272-72021b44-33d3-4576-b20c-c240aef6527f.png)

Tiedostolla Index on ei-pysyvä yhteys sovelluslogiikasta vastaavaan AppFunctions-luokkaan, jolla taas on pysyvä yhteys db_modules moduuliin, joka sisältää tietokannan käyttöön tarkoitetut funktiot.




## Käyttöliittymä

Käyttöliittymän luokka App on sovelluksen pääluokka ja se perii ttk.Window-luokan ja määrittelee esimerkiksi ikkunan koon, fontin ja ttkbootstrap-teeman ja käynnistää pääsilmukan. 

Sovelluksen osa-alueet kuten kirjautumislomake on jaettu widgetteihin/komponentteihin jotka toteuttavat aina jonkin ominaisuuden. Komponentit käyttävät luokassa Data määriteltyjä muuttujia tiedon tallentamiseen ja komponentin päivittämiseen ja tiedon välittämiseen muille komponenteille sekä App-luokalle.

App piilottaa osan komponenteista sovelluksen käynnistyksessä ja komponentit määrittelevät ne näkyviin tarvittaessa. App sisältää lisäksi metodit näytön keskikohdan määrittämiseen, uloskirjautumiseen ja käyttäjän sivun päivittämiseen. TkInter layoutin tekemisessä on käytetty grid-metodia. Käyttöliittymäkoodista kutsutaan aina tarvittaessa app_functions-tiedoston metodeja, koska siellä sijaitsee sovelluslogiikka.
