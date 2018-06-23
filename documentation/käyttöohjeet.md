# Käyttöohjeet



---

## Tavallinen selaaja 

Tavallisen, rekisteröitymättömän selaajan on mahdollista selata sovelluksen tarjoamia matkakohteita painamalla sivuston yläpalkin "Destinations"-nappia. 

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_destinations.png" width=900>

Avautuu tarjolla olevien matkakohteiden lista, jossa kohteet ovat suosituimmuusjärjestyksessä. Kohteen nimeä klikkaamalla selaaja saa tarkempaa tietoa kyseisestä kohteesta - erityisesti selaaja löytää kohteessa tarjolla olevien majoitusvaihtoehtojen listan.

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_italia.png" width=900>

Majoitusvaihtoehdot ovat samoin saamiensa "tykkäämisten" mukaisessa järjestyksessä. Majoitusvaihtoehdon nimeä klikkaamalla selaaja pääsee tarkemmin tutustumaan kyseisen kohteen ominaisuuksiin ja siellä tarjolla oleviin huonetyyppeihin. 

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_ca'diLori.png" width=900>

Huonetyyppien tiedot on kirjattu listaan, jossa huonetyypit ovat hintansa ja majoittajamääränsä mukaisessa järjestyksessä. Sivun alareunassa ovat käytettyjen pikkukuvakkeiden selitykset.

Selaajan on myös mahdollista luoda sovellukseen oman käyttäjätunnuksensa. Tämä tapahtuu klikkaamalla sivuston yläreunan "Login"-painiketta ja edelleen avautuvan näkymän vasemmassa yläreunassa olevaa "New account" -nappia. 

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_new_user.png" width=900>

Sovellus esittää lomakkeen, jonka jokaiseen kenttään on vastattava. Virheellisen tiedon tapauksessa "Sign up" -nappia painettaessa sovellus antaa virheilmoitukset punaisessa laatikossa, kentän rivien mukaan. Mikäli selaaja yrittää luoda käyttäjätunnuksen jo olemassa olevalla käyttäjänimellä, pyytää sovellus selaajaa vaihtamaan käyttäjänimeä. Kun kaikki lomakkeen tiedot ovat virheettömiä, sovellukseen luodaan uusi käyttäjätunnus "Sign up" -napin painalluksella.


---
## 2) Rekisteröitynyt käyttäjä

Rekisteröitynyt käyttäjä pääsee kirjautumaan sisään sovellukseen sivuston yläpalkin "Login"-nappia painamalla. 

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_login.png" width=900>

Sovellus pyytää käyttäjän käyttäjänimeä ja salasanaa sekä tarkistaa annetut tiedot käyttäjän painaessa sisäänkirjautumisnäkymän "Login"-nappia. 

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_kirjautuminen.png" width=900>

Virheellisestä tiedosta ilmoitetaan. Rekisteröityneen käyttäjän ollessa sisäänkirjautunut ilmoittaa sovellus kirjautuneena olevan käyttäjän nimen sivuston yläpalkissa muodossa "Logged in as...". Tämän ohessa on kohta "Logout", jota klikkaamalla käyttäjän on mahdollista kirjautua ulos sovelluksesta.

Kun rekisteröitynyt käyttäjä on kirjautunut sisään tunnuksillaan, on käyttäjän mahdollista selata sovelluksen tarjoamia matkakohteita ja niiden majoitusvaihtoehtoja samaan tapaan, kuin yllä esitettiin tavallisen selaajan tapauksessa. Erona tavallisen selaajan tilanteeseen on se, että rekisteröityneen käyttäjän on mahdollista "tykätä" sekä valitsemastaan matkakohteesta että majoitusvaihtoehdosta kunkin omalla sivulla. 

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_like.png" width=900>

"Tykkääminen" tapahtuu "Like"-nappia painamalla, ja samasta kohteesta voi "tykätä" vain kerran. Mikäli kirjautunut käyttäjä on jo "tykännyt" kohteesta, ilmoittaa sovellus tästä tekstillä "You have already liked". 

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_liked.png" width=900>

Lisäksi rekisteröityneelle käyttäjälle on tarjolla huoneen varaaminen valitsemansa matkakohteen valitsemassaan majoitusvaihtoehdossa. Jos majoitusvaihtoehdon huonetyyppi on edelleen tarjolla - se ei ole varattu täyteen - on huonetyypin rivillä "Book"-nappi. Muussa tapauksessa napin paikalla lukee "Fully Booked", eikä nappia ole mahdollista painaa. 

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_select_book.png" width=900>

"Book"-nappia painamalla rekisteröitynyt käyttäjä siirtyy varaamiseen. Varausnäkymässä ilmoitetaan tehtävän varauksen tiedot ja pyydetään käyttäjää valitsemaan sekä varattavien öiden määrä että varausvahvistuksen toimitus sähköpostitse ja/tai tekstiviestillä. "Book"-napin painaminen johtaa varauksen lähettämiseen vain, jos öiden määrä on valittu ja jompikumpi tai molemmat toimitusvaihtoehdoista ovat valittuna.

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_book.png" width=900>

Sekä onnistunut varaaminen että sivuston yläpalkin "My page"-kohdan painaminen johtaa rekisteröityneen käyttäjän omalle sivulle. Omalla sivulla esitetään kirjautuneena olevan käyttäjän tiedot ja kyseiseen käyttäjään liittyvät varauspyynnöt. Sovelluksen ylläpitäjän hyväksymät varauspyynnöt ovat omassa listassaan, samoin vielä hyväksyntää odottavat varauspyynnöt, jotka käyttäjä voi halutessaan peruuttaa varausnumeron alla olevaa roskakorinappia painamalla. 

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_my_page.png" width=900>

Näkymän alla olevan isomman roskakorinapin painaminen poistaa kirjautuneena olevan käyttäjätunnuksen tietoineen. Kynänappi puolestaan mahdollistaa käyttäjätietojen muokkaamisen ja lukkonappi salasanan vaihdon. Tietojen muokkaussivulla muokattavien käyttäjätietojen kentissä on oletuksena tämänhetkinen sovelluksen muistissa oleva tieto. Muutokset saa voimaan "Change"-nappia painamalla, virhetapauksessa sivun alareunaan punaiseen laatikkoon ilmestyy lista virheilmoituksista. Salasanan vaihtamisen yhteydessä kysytään käyttäjän vanhaa salasanaa. Ainoastaan oikean salasanan syöttäminen ja uuden 7 merkkiä pitkän salasanan antaminen johtaa salasanan vaihtoon.


---
## 3) Ylläpitäjä

Ylläpitäjän käyttäjänimi on sovelluksessa aina muotoa "admin". Kirjautuminen ja uloskirjautuminen tapahtuu samaan tapaan kuin rekisteröityneen käyttäjän tapauksessa. 

Kuten muidenkin käyttäjäroolien on ylläpitäjänkin mahdollista selata tarjolla olevia matkakohteita ja niiden majoitusvaihtoehtoja. Tavallisen selaajan tapaan ylläpitäjän ei ole mahdollista "tykätä" kohteista. Sen sijaan matkakohdenäkymän alareunassa olevalla roskakorinapilla ylläpitäjä voi poistaa matkakohteen, estonapilla laittaa matkakohteen syrjään, kynänapilla muokata matkakohteen tietoja ja tenttanapilla lisätä matkakohteeseen uuden majoitusvaihtoehdon. Sekä matkakohteen tietoja muokattaessa että uuden majoitusvaihtoehdon lisäämisen yhteydessä sovellus tarkistaa annetun tiedon oikeellisuuden ja esittää virheilmoitukset tarvittaessa. 

Poiston ja eston erona on se, että ensiksi mainitun poistaessa kohteen kokonaan sovelluksesta syrjään siirtäminen mahdollistaa kohteeseen jo tehtyjen varausten säästämisen. Tämän vuoksi poistaminen on mahdollista vain kohteille, joihin ei ole tehty varauksia. Kun kohde siirretään syrjään, ainoastaan ylläpitäjän on mahdollista nähdä kohde matkakohteiden listalla. Myös kaikki kohteeseen liittyvät majoitusvaihtoehdot siirretään syrjään. Ylläpitäjä voi edelleen tarkastella syrjässä olevien kohteiden tietoja, vaikka tietojen muokkaaminen ei ole mahdollista. Ylläpitäjän voi myös palauttaa kohteen takaisin tarjolla olevaan valikoimaan.

Majoitusvaihtoehdon näkymässä sivun alareunassa on poisto- (roskakorinappi), esto- () ja muokkaustoimintojen (kynänappi) lisäksi mahdollista lisätä majoitusvaihtoehtoon sovellukseen luotuja huonetyyppejä. Huonetyyppien lisäykseen päästään plusnappia painamalla. Avautuu lista niistä huonetyypeistä, joita majoitusvaihtoehtoon ei vielä ole lisätty. Kunkin huonetyypin nimeä esittävää nappia painamalla kyseinen huonetyyppi lisätään majoitusvaihtoehtoon - samassa näkymässä pysytään siis mahdollisesti useamman huonetyypin lisäämisen ajan. Vasta "Done"-napin painaminen palauttaa ylläpitäjän majoitusvaihtoehdon näkymään. Majoitusvaihtoehdossa tarjolla olevien huonetyyppien listaan ovat ilmestyneet lisätyt huonetyypit. Huonetyypin voi myös poistaa majoitusvaihtoehdosta klikkaamalla huonetyypin nimen alla olevaa roskakorinappia. Huonetyypin poistaminen kyseisestä majoitusvaihtoehdosta ei poista sitä koko sovelluksesta.

Sivuston yläpalkin "New destination" tai "New room-type" -nappia painamalla ylläpitäjä voi lisätä sovellukseen uuden matkakohteen tai uuden huonetyypin. "Add"-napin painaminen tiedonsyötön jälkeen toteuttaa lisäyksen. Virheellisen tiedon tapauksessa sovellus esittää sivun alalaidassa, punaisessa laatikossa tapauskohtaiset virheilmoitukset.

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_new_roomtype.png" width=900>

"Bookings"-kohtaa sivuston yläpalkissa painettaessa ylläpitäjä saa näkyviinsä tiedot koskien tehtyjä varauksia. Näkymässä on tarkka lista kaikista tehdyista varauspyynnöistä tietoineen. Varauspyynnöt ovat järjestyksessä sen mukaan, mikä niistä on lähetetty ajallisesti ensimmäisenä. 

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_all_bookings.png" width=900>

Listauksen oikeassa reunassa kunkin varauspyynnön kohdalla on joko oranssi merkki tai "Approve"-nappi. Oranssi merkki tarkoittaa, että ylläpitäjä on hyväksynyt rekisteröityneen käyttäjän lähettämän varauspyynnön ja samalla toimittanut käyttäjälle automaattisesti varausvahvistusviestin käyttäjän toivomalla tavalla (vieressä olevat kirjekuori- ja/tai puhelinkuvakkeet). Vielä tähän mennessä hyväksymättömät varaukset voidaan ylläpitäjän toimesta hyväksyä kunkin varauspyynnön "Approve"-nappia painamalla. Napin painamisen seurauksena varauspyyntö hyväksytään, ja napin korvaa oranssi merkki.

"Bookings"-sivulla on toisaalta sovelluksen ylläpitäjälle tärkeää statistiikkaa.

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_statics.png" width=900>

Lehdellä kerrotaan, miten monta varausta kuhunkin rekisteröityneeseen käyttäjään liittyy ja kuinka suosittuja eri matkakohteet, majoitusvaihtoehdot sekä huonetyypit ovat olleet.

Varauksen hinta muodostuu kolmesta tekijästä: huonetyypin hinnasta, majoituskohteelle ominaisesta hintakertoimesta ja käyttäjän valitsemasta majoituspäivien määrästä. Huonetyypin hinta määritellään huonetyypin luomisen yhteydessä ja on kaikissa majoitustapauksissa sama. Yksittäisessä majoituskohteessa tarjolla olevan huoneen hinta tosin määräytyy majoituskohteen hintakertoimen mukaan (huonetyypin hinta x majoituskohteen hintakerroin). Hintakerroin on välillä 0.5-2.0. Varausta tehdessään käyttäjä valitsee, kuinka moneksi päiväksi hän huoneen haluaa varata. Majoituskohtainen huoneen hinta kerrotaan valittujen päivien määrällä.

Jotta ylläpitäjän on mahdollista tarkastella sovelluksen sisältämää dataa helposti ja nopeasti, pääsee ylläpitäjä käsiksi dataan sivuston yläpalkin "Navigation"-kohtaa klikkaamalla. Avautuvalla sivulla listataan erikseen kaikki sovelluksen matkakohteet, majoitusvaihtoehdot ja huonetyypit aakkosellisessa järjestyksessä. Nimen kohdalla huomautetaan, mikäli tietokohde on varauksilta syrjässä. Kutakin nimeä klikkaamalla siirrytään valitun kohteen tietojen näkymään.

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_navigation.png" width=900>

Kun ylläpitäjä tarkastelee "Navigation"-sivun kautta huonetyyppikohtaisia tietoja, ilmoitetaan ylläpitäjälle, missä sovelluksen tarjoamista majoitusvaihtoehdoista kyseinen huonetyyppi on tarjolla. 

<img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/Kaukokaipuu_roomtype.png" width=900>

Lisäksi ylläpitäjän on mahdollista poistaa huonetyyppi sivun alareunan roskakorinappia painamalla, siirtää huonetyyppi syrjään tai muokata huonetyypin tietoja kynänappia painamalla. Huonetyypin poistaminen poistaa sen kaikista niistä majoitusvaihtoehdoista, joihin se oli ennen poistoa kirjattuna. Samoin kuin edellä, ainoastaan huonetyypit, joita ei ole lainkaan varattu, voidaan poista. Huonetyypin tietojen muokkaamisen yhteydessä sovellus tarkistaa syötetyn tiedon oikeellisuuden ja esittää tarpeen mukaan tapauskohtaiset virheilmoitukset.
