# User stories ja keskeiset SQL-kyselyt

---

## User stories

(Toimintoa seuraava numero viittaa taulukon alla olevaan listaan keskeisimmistä SQL-kyselyistä.)

Käyttäjärooli | Mitä | Miksi
------------ | ------------- | -------------
Ylläpitäjä | Sisäänkirjautuminen ylläpitäjänä | Ylläpitäjällä ainoastaan on lupa muuttaa sovelluksen sisältöä
Ylläpitäjä | Uloskirjautuminen ylläpitäjänä | Jotta kukaan ulkopuolinen ei pääse päivittämään sovelluksen sisältöä
Ylläpitäjä | Matkakohteiden lisääminen | Jotta sovelluksen matkakohdelista vastaisi tarjontaa
Ylläpitäjä | Matkakohteiden poistaminen | Jotta kannattamattomat kohteet voidaan poistaa
Ylläpitäjä | Matkakohteiden laittaminen syrjään | Jotta tieto aiemmista varauksista säilyy tietokannassa vaikka kohde ei ole enää varattavissa
Ylläpitäjä | Matkakohteiden palauttaminen varattavaksi | Jotta kohde saadaan takaisin valikoimaan
Ylläpitäjä | Matkakohteiden päivittäminen | Matkakohteen kuvausta päivittämällä lisätään kohteen kiinnostavuutta
Ylläpitäjä | Majoituskohteiden lisääminen matkakohteeseen | Jotta matkakohteen majoitusvalikoima vastaisi tarjontaa
Ylläpitäjä | Majoituskohteiden poistaminen matkakohteesta | Jotta kannattamattomat kohteet voidaan poistaa
Ylläpitäjä | Majoituskohteiden laittaminen syrjään | Jotta tieto aiemmista varauksista säilyy tietokannassa vaikka kohde ei ole enää varattavissa
Ylläpitäjä | Majoituskohteiden palauttaminen varattavaksi | Jotta kohde saadaan takaisin valikoimaan
Ylläpitäjä | Majoituskohteiden päivittäminen | Majoituskohteen houkuttavuus on sitä parempi, mitä tarkemmin sitä kuvataan
Ylläpitäjä | Huonetyyppien lisääminen | Jotta majoituskohteisiin voidaan lisätä haluttuja huonetyyppejä
Ylläpitäjä | Huonetyyppien poistaminen | Jotta turhat huonetyypit eivät vie muistitilaa
Ylläpitäjä | Huonetyypin laittaminen syrjään | Jotta tieto aiemmista varauksista säilyy tietokannassa vaikka huonetyyppi ei ole enää varattavissa
Ylläpitäjä | Huonetyypin palauttaminen varattavaksi | Jotta huonetyyppi saadaan takaisin valikoimaan
Ylläpitäjä | Huonetyyppien päivittäminen | Jotta huonetyyppi vastaa olemassa olevaa
Ylläpitäjä | Huonetyyppien lisääminen majoituskohteeseen (1)| Jotta majoituskohteen huonevalikoima vastaisi tarjontaa
Ylläpitäjä | Huonetyyppien poistaminen majoituskohteesta (2)| Jotta majoituskohteen huonevalikoima vastaisi tarjontaa
Ylläpitäjä | Varausten tarkastelu (3)| Ylläpitäjän on mahdollista nähdä lista saapuneista varauksista; varaukset esitetään listalla niiden saapumisjärjestyksessä (ensiksi tullut ylimpänä)
Ylläpitäjä | Tilausvahvistusten lähettäminen | Ylläpitäjän on mahdollista klikata varaus vahvistetuksi ja samalla toimittaa tilausvahvistusviesti asiakkaan toivomalla tavalla (sähköpostitse tai tekstiviestillä)
Ylläpitäjä | Varausstatistiikan seuraaminen (4), (5)| Ylläpitäjän on mahdollista nähdä tilastotietoa siitä, miten asiakkaat ovat sovellusta käyttäneet ja miten paljon eri kohteita/majoitusvaihtoehtoja/huonetyyppejä on varattu 
Asiakas | Käyttäjätunnuksen luominen | Jotta asiakkaan on mahdollista tehdä varauksia käyttäjätunnuksellaan
Rek. Asiakas | Sisäänkirjautuneena käyttäjätunnuksen poistaminen | Jotta asiakkaan on mahdollista halutessaan lopettaa sovelluksen käyttäminen
Rek. Asiakas | Sisäänkirjautuneena käyttäjätunnuksen tietojen muokkaaminen | Jotta asiakkaan on mahdollista päivittää henkilötietojaan
Rek. Asiakas | Sisäänkirjautuneena käyttäjätunnuksen salasanan vaihtaminen | Asiakkaan turvallisuus taataan mahdollistamalla salasanan vaihtaminen
Rek. Asiakas | Käyttäjätunnuksella sisään kirjautuminen | Asiakkaan on mahdollista kirjautua sisään käyttäjätunnuksellaan ja tehdä varauksia
Rek. Asiakas | Käyttäjätunnuksella ulos kirjautuminen | Jotta kukaan ulkopuolinen ei pääse tarkastelemaan asiakkaan käyttäjätietoja
Asiakas/Rek. Asiakas | Matkakohdelistan tarkastelu | Asiakkaan on mahdollista tarkastella matkakohteita joko kirjautuneena tai ei; matkakohteet ovat listalla saamiensa "tykkäysten" määrän mukaisessa järjestyksessä (eniten "tykkäyksiä" saanut ylimpänä)
Asiakas/Rek. Asiakas | Matkakohteen lähempi tarkastelu | Asiakkaan on mahdollista klikata matkakohdetta ja lukea tarkempaa tietoa kohteesta
Asiakas/Rek. Asiakas | Matkakohteen majoitusvalikoiman tarkastelu (6)| Asiakkaan on mahdollista tarkastella klikkaamansa matkakohteen majoitusvalikoimaa; majoitusvaihtoehdot ovat listalla saamiensa "tykkäysten" määrän mukaisessa järjestyksessä (eniten "tykkäyksiä" saanut ylimpänä)
Asiakas/Rek. Asiakas | Majoituskohteen lähempi tarkastelu | Asiakkaan on mahdollista klikata matkakohteen majoitusvaihtoehtoa ja lukea tarkempaa tietoa siitä
Asiakas/Rek. Asiakas | Majoituskohteen huonevalikoiman tarkastelu (7)| Asiakkaan on mahdollista tarkastella klikkaamansa majoituskohteen huonevalikoimaa
Rek. Asiakas | Sisäänkirjautuneena majoituskohteen vapaiden huonetyyppien tarkastelu (8)| Kirjautuneen asiakkaan on mahdollista nähdä klikkaamansa majoituskohteen vapaana olevat huonetyypit
Asiakas/Rek. Asiakas | Matkakohteen/majoituspaikan "tykkäysten" tarkastelu (9)| Asiakkaan on mahdollista tarkastella matkakohteiden ja majoituspaikkojen "tykkäyksiä"
Rek. Asiakas | Sisäänkirjautuneena "tykkääminen" (10)| Asiakkaan on mahdollista "tykätä" matkakohteesta tai majoitusvaihtoehdosta ainoastaan sisään kirjautuneena; sama asiakas voi "tykätä" jokaisesta tietokohteesta vain kerran
Rek. Asiakas | Sisäänkirjautuneena varauksen tekeminen | Asiakkaan on mahdollista varata matka tietyn matkakohteen majoitusvaihtoehdon vapaaseen huoneeseen; varauksen yhteydessä asiakas päättää varattavien öiden määrän; varauksen yhteydessä asiakas voi määritellä, lähetetäänkö hänelle onnistuneesta varauksesta tilausvahvistusviesti sähköpostitse vai tekstiviestillä; varauksen yhteydessä asiakkaalle annetaan varausnumero
Rek. Asiakas | Sisäänkirjautuneena "My page" -osion tarkastelu (11)| Asiakkaan on mahdollista tarkastella tekemiään varauksia "My page" -osiossa; varaustietojen ohessa lukee, onko varaus vahvistettu
Rek. Asiakas | Sisäänkirjautuneena vahvistamattomien varauspyyntöjen poistaminen | Asiakkaan on mahdollista poistaa vahvistamattomia varauksia "My page" -osiossa


---

## Keskeisimmät SQL-kyselyt

### 1) Huonetyypit, joita ei ole vielä lisätty majoituskohteeseen

SELECT RoomType.id, RoomType.unavailable, RoomType.name, RoomType.size  
FROM RoomType  
WHERE NOT EXISTS (SELECT association.roomtype_id FROM association  
WHERE association.roomtype_id = RoomType.id  
AND association.accomodation_id = :accomodation)  
ORDER BY RoomType.size, RoomType.name

### 2) Huonetyypin poistaminen majoituskohteesta

DELETE FROM association  
WHERE (association.accomodation_id = :accomodation  
AND association.roomtype_id = :roomtype)

### 3) Kaikki tehdyt varauspyynnöt tietoineen

SELECT Booking.id, Booking.booking_number, Booking.date_created, Booking.approved, Booking.nights, Booking.price, Booking.email_notification, Booking.phone_notification, RoomType.name, RoomType.size, Accomodation.name, Destination.name, Client.name  
FROM Booking, RoomType, association, Accomodation, Destination, Client  
WHERE Booking.client_id = Client.id  
AND Booking.roomtype_id = RoomType.id  
AND RoomType.id = association.roomtype_id  
AND association.accomodation_id = Accomodation.id  
AND Booking.accomodation_id = Accomodation.id  
AND Accomodation.destination_id = Destination.id  
ORDER BY Booking.date_created

### 4) Asiakkaiden tekemien varausten määrät

SELECT Client.name, COUNT(Booking.id)  
FROM Client  
LEFT JOIN Booking ON Booking.client_id = Client.id  
WHERE Client.username != 'admin'  
GROUP BY Client.id  
ORDER BY Client.name

### 5) Matkakohteiden varausten määrät

(Sama kysely koskien majoituskohteiden ja huonetyyppien varausten määriä)

SELECT Destination.name, COUNT(Booking.id) AS count  
FROM Destination  
LEFT JOIN Accomodation ON Destination.id = Accomodation.destination_id  
INNER JOIN Booking ON Accomodation.id = Booking.accomodation_id  
GROUP BY Destination.id  
ORDER BY count DESC, Destination.name ASC

### 6) Tietyn matkakohteen majoitusvaihtoehdot suosittuusjärjestyksessä

(Sama matkakohteiden listauksessa suosittuusjärjestyksessä)

SELECT Accomodation.id, Accomodation.name, Accomodation.unavailable, COUNT(LikeAccomodation.id) AS likes  
FROM Accomodation  
LEFT JOIN LikeAccomodation ON LikeAccomodation.accomodation_id = Accomodation.id  
WHERE (Accomodation.destination_id = :destination)  
GROUP BY Accomodation.id  
ORDER BY likes DESC  

### 7) Tietyssä majoituskohteessa tarjolla olevat huonetyypit

SELECT RoomType.id, RoomType.unavailable, RoomType.name, RoomType.size, RoomType.price, RoomType.many, RoomType.seaside_view, RoomType.air_conditioned, RoomType.mini_bar, RoomType.tv, RoomType.bath, COUNT(DISTINCT Booking.id)  
FROM Accomodation  
INNER JOIN Booking ON :accomodation = Booking.accomodation_id  
RIGHT JOIN RoomType ON Booking.roomtype_id = RoomType.id  
INNER JOIN association ON RoomType.id = association.roomtype_id  
WHERE association.accomodation_id = :accomodation  
GROUP BY RoomType.id, RoomType.unavailable, RoomType.name, RoomType.size, RoomType.price, RoomType.many, RoomType.seaside_view, RoomType.air_conditioned, RoomType.mini_bar, RoomType.tv, RoomType.bath  
ORDER BY RoomType.size, RoomType.price

### 8) Huonetyypin varausten määrä tietyssä majoituskohteessa
 
SELECT RoomType.id, COUNT(Booking.id)  
FROM RoomType  
LEFT JOIN Booking ON RoomType.id = Booking.roomtype_id  
WHERE Booking.accomodation_id = :accomodation  
GROUP BY RoomType.id  
ORDER BY RoomType.size, RoomType.name

### 9) Miten monta "tykkäystä" majoituskohde on saanut

(Sama koskien matkakohteen saamien "tykkäysten" määrää)

SELECT COUNT(LikeAccomodation.id)  
FROM LikeAccomodation  
WHERE LikeAccomodation.accomodation_id = :accomodation

### 10) Onko asiakas "tykännyt" majoituskohteesta

(Sama koskien sitä, onko asiakas "tykännyt" matkakohteesta)

SELECT COUNT(LikeAccomodation.id)  
FROM LikeAccomodation  
WHERE LikeAccomodation.client_id = :client  
AND LikeAccomodation.accomodation_id = :accomodation

### 11) Vahvistetut/vahvistamattomat asiakkaan varauspyynnöt

SELECT Booking.id, Booking.booking_number, Booking.date_created, Booking.price, Booking.nights, Booking.email_notification, Booking.phone_notification, RoomType.name, RoomType.size, Accomodation.name, Destination.name  
FROM Booking, RoomType, association, Accomodation, Destination  
WHERE (Booking.client_id = :client AND Booking.approved = :approved)  
AND Booking.roomtype_id = RoomType.id  
AND RoomType.id = association.roomtype_id  
AND association.accomodation_id = Accomodation.id  
AND Booking.accomodation_id = Accomodation.id  
AND Accomodation.destination_id = Destination.id  
ORDER BY Booking.date_created
