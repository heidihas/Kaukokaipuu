# Työn rajoitteet ja puuttuvat ominaisuudet

---

## Rajoitteet

Jotta sovellus muistuttaisi todellista matkanvarausjärjestelmää, tulisi saman huoneen olla varattavissa useammin kuin kerran. Tämänhetkinen toteutus mahdollistaa valitun majoitusvaihtoehdon huoneen varaamisen ainoastaan kerran. Jos hotellissa on esimerkiksi kaksi sviittiä, voi ainoastaan kaksi rekisteröitynyttä käyttäjää varata hotellista sviitin. Yksinkertaistuksen vuoksi myös oletetaan, että tietyn huonetyypin huoneita on eri hotelleissa aina sama määrä tarjolla. Esimerkiksi sviittiä olisi kaksi niin Hotel Kämpissä kuin Hotelli Eirassa, mikäli hotelliin on yhdistetty huonetyyppi "sviitti".

Sovelluksen matkakohteiden, majoitusvaihtoehtojen ja huonetyyppien osalta on käytössä ominaisuus tietokohteen asettamiseksi syrjään. Näin tietokohde ei katoa tietokannasta (etuna siihen liittyvien varausten säilyminen) vaan asetetaan käyttäjien varauksilta sivuun. Tosin syrjään asettaminen ei ole mahdollista tietyn majoitusvaihtoehdon tarjoamiin huonetyyppeihin eli yhdistäminen taulujen Accomodation ja RoomType väliseen liitostauluun. Oletetaan, että hotelliin lisätty huonetyyppi on aina tarjolla ja että huonetyyppi voidaan poistaa hotellista ainoastaan silloin, kun siihen ei ole tehty yhtään varausta (esimerkiksi ylläpitäjän virheellisen sovelluksen käytön tapauksessa). Tällöin hotellin tarjolla olevien huonetyyppien tulisi olla hyvin tiedossa majoitusvaihtoehdon luomisen yhteydessä, eikä valikoima saisi muuttua.

Tietokohteiden syrjään laittaminen on siltä osin hyvä ratkaisu, että tieto joskus varattavissa olleista kohteista säilyy muistissa - ainoa tapa päästä kohteesta "eroon" ei ole sen poistaminen. Malli mukailee monessa sovelluksessa käytössä olevaa toimintatapaa. Toisaalta tehtyjä varauksia koskevien tietojen säilyvyyden kannalta tietokohteiden laittaminen syrjään ei kenties ole paras peruste. Varaustiedot voitaisiin esimerkiksi tallettaa erilliseen tiedostoon, jolloin tiedot olisivat turvassa tietokohteiden muutoksilta. Sovelluksen tarjoaja voisi vedota siihen, että oikeudet muutoksiin on pidätetty. Tällöin tietokohteiden muokkaaminen varauspyynnön lähettämisen jälkeen olisi sallittua. Tämä menettely voisi toimia varauspyynnöissä, joita ei ole vielä vahvistettu. Vahvistettujen varausten tapauksessa asiakassuojan piiriin kuuluisi se, ettei esimerkiksi varauksen hinta muutu varauspyynnön vahvistamisen jälkeen.


---

## Puuttuvat ominaisuudet

Jotta matkanvarausjärjestelmä olisi realistisempi, tulisi sovelluksella olla käytössä varauskalenteri. Sama huone voitaisiin varata useamman kerran, kuitenkin niin ettei mikään varaus menisi ajallisesti toisen kanssa päällekkäin. Tietyn majoitusvaihtoehdon tarjoamia huonetyyppejä voisi myös laittaa sivuun eli estää käyttäjiä varaamasta kyseisen huonetyypin huoneita, vaikka itse huonetyyppiä ei poistettaisikaan kokonaan majoitusvaihtoehdosta.

Asiakkaan selaamista helpottaisi ja nopeuttaisi se, jos matkakohteen sivulla olevalla majoitusvalikoimalistalla ilmoitettaisiin suoraan, onko tietyssä hotellissa tilaa vai ei. Käyttäjän ei täytyisi klikata majoitusvaihtoehdon omalla sivulle todetakseen, että kaikki huoneet ovat jo varattuja. Toisaalta joissakin tapauksissa niin asiakkaiden kuin ylläpitäjän käyttöä helpottaisi näkymien sivutus.
