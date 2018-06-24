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

Mikäli toimijalla ei ole olemassa omaa tunnusta Github-palvelussa, on toimijan ensin rekisteröidyttävä. Rekisteröitymisen jälkeen Githubiin on luotava uusi repositorio sovellusta varten. Github-repositorion osoitteen saa selville Githubista.

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
