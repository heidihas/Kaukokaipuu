# Asennusohjeet


---

Ohessa esitetään vaiheittain ohjeet sovelluksen asentamiseen.

## Hakemiston lataaminen omalle tietokoneelle

Sovelluksen sisältävän git-repositorion [etusivulla](https://github.com/heidihas/Kaukokaipuu/) on oikeassa reunassa vihreä painike "Clone or download", jota painamalla ja valitsemalla "Download ZIP" projekti saadaan ladattua omalle tietokoneelle. Ladattu tiedostopaketti tulee purkaa, minkä jälkeen sovelluksen hakemisto on käytettävissä.

## Virtuaaliympäristön luominen

Aluksi on mentävä päätteellä sovellushakemiston juureen. Alla olevalla komennolla saadaan luotua hakemistoon Python-virtuaaliympäristö.
```
python3 -m venv venv
```
Aktivoidaan Python-ympäristö käyttöön komennolla:
```
source venv/bin/activate
```
Mikäli käytössä oleva pip on vanhentunut, voidaan se päivittää komennolla:
```
pip install --upgrade pip
```
Mikäli käytössä olevasta tietokoneesta puuttuu Flask-liitännäinen, saadaan se ladattua komennolla:
```
pip install Flask
```
Sovelluksen riippuvuudet saadaan asennettua virtuaaliseen ympäristöön alla olevalla komennolla.
```
pip install -r requirements.txt
```

## Sovelluksen siirtäminen Githubiin

Mikäli toimijalla ei ole olemassa omaa tunnusta Github-palvelussa, on toimijan ensin [rekisteröidyttävä](https://github.com/join?source=header-home). Rekisteröitymisen jälkeen Githubiin on luotava uusi repositorio sovellusta varten. Github-repositorion osoitteen saa selville Githubista.

Projektikansiolle luodaan git-versionhallinta komennolla:
```
git init
```
Githubissa oleva repositorio lisätään kansion paikallisen versionhallinnan etäpisteeksi komennolla:
```
git remote add origin "github-projektin-osoite"
```
Lopuksi tiedostot saadaan siirrettyä Githubiin alla olevilla komennoilla.
```
git add .
```
```
git push -u origin master
```

## Sovelluksen siirtäminen Herokuun

Python-virtuaaliympäristön ollessa jo aktivoituna voidaan sovellukselle lisätä web-palvelin Gunicorn, jotta siirtäminen Herokuun olisi mahdollista. Lisääminen onnistuu alla olevalla komennolla.
```
pip install gunicorn
```
Koska ladatussa sovellushakemistossa on jo valmiina tiedostot requirements.txt ja Procfile, ei niitä tarvitse alustaa uudestaan.

Mikäli toimijalla ei ole vielä omaa tunnusta Herokussa, on toimijan [rekisteröidyttävä](https://signup.heroku.com/?c=70130000001x9jFAAQ) palveluun. Käytössä olevan tietokoneen komentorivillä on myös oltava Herokun työvälineet, jotka voidaan tarvittaessa ladata Internetistä löytyvillä [ohjeilla](https://devcenter.heroku.com/articles/heroku-cli).

Herokuun voi kirjautua sisään komentoriviltä komennolla
```
heroku login
```
ja syöttämällä pyydetyt tiedot. Paikan luominen Herokuun onnistuu alla olevalla komennolla, jota varten tarvitaan sovellukselle uniikki nimi. Jos nimen jättää pois komennosta, luo Heroku sovellukselle satunnaisen nimen.
```
heroku create "sovelluksen-nimi"
```
Kun sovelluksella on paikka Herokussa, saadaan paikalliseen versionhallintaan tieto Herokusta komennolla:
```
git remote add heroku "git.heroku.com-muotoinen-osoite-jonka-heroku-sovellukselle-antaa"
```
Projekti saadaan lähetettyä Herokuun komennoilla:
```
git add .
```
```
git commit -m "Initial commit"
```
```
git push heroku master
```
Sovellus on katseltavissa osoitteessa https://"sovelluksen-nimi".herokuapp.com/. Jos sovellukseen on tullut päivityksiä, on muutokset myös hyvä lähettää Githubiin.
```
git push origin master
```
Mikäli sovelluksen tiedostoja ja ominaisuuksia halutaan kehittää edelleen, on hyvä laittaa päälle Herokun sivuilla automaattinen tiedonvälitys käytössä olevasta git-repositoriosta Herokuun. Tämä onnistuu kirjautumalla sisään Herokun nettisivuilla ja muokkaamalla kyseiseen sovellukseen liittyviä asetuksia.

## PostgreSQL-tuen lisääminen

Koska sovelluksen ei haluta toimivan paikallisesti SQLiteä käyttäen, on sovellukseen lisättävä PostgreSQL-tuki. PostgreSQL-tietokannanhallintajärjestelmän käyttöä varten tarvitaan psycopg2-ajuri.
```
pip install psycopg2
```
Sovelluksen käyttöön saadaan tieto siitä, että se on Herokussa komennolla:
```
heroku config:set HEROKU=1
```
Tietokanta ei siirry automaattisesti Herokuun, vaan se on lisättävä komennolla:
```
heroku addons:add heroku-postgresql:hobby-dev
```
Nyt sovellus on halutulla tavalla Herokussa ja toimii itsenäisesti Herokun omalla tietokannalla.
