# Tietokannan rakenne

## Tietokannan taulut ja tietokantakaavio

Sovelluksessa käytettävä tietokanta koostuu seitsemästä varsinaisesta taulusta ja yhdestä liitostaulusta. Taulut kuvaavat sovelluksen kannalta merkittäviä käsitteitä: asiakasta, matkakohdetta, majoituskohdetta, huonetyyppiä, varausta ja "tykkäystä". Liitostaulu puolestaa mahdollistaa kahden taulun välille monesta moneen -suhteen.

<p align="center">
  <img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/kaukokaipuu_tietokantakaavio.jpg">
</p>

Taulun Client rivit kuvaavat rekisteröityneitä asiakkaita. Client-taulusta on yhden suhde moneen -relaatio Booking-tauluun, sillä sama asiakas voi tehdä useamman varauksen, mutta yhteen varaukseen liittyy aina vain yksi asiakas. Toisaalta asiakkaan on mahdollista "tykätä" sovelluksen tarjoamista matka- ja majoituskohteista. Tätä varten Client-taulusta on yhden suhde moneen -relaatio myös tauluihin LikeDestination ja LikeAccomodation.

Koska sekä taulu LikeDestination että taulu LikeAccomodation kuvaavat eräänlaista asiakkaan "suhdetta" joko matka- tai majoituskohteeseen, liittyy kumpaankin tauluun kaksi viiteavainta. Asiakas voi tehdä useita "tykkäyksiä", mutta "tykkäykseen" liittyy vain yksi asiakas. Samoin matka- tai majoituskohteesta on voitu "tykätä" monesti, mutta yksi "tykkäys" kohdistuu vain tiettyyn kohteeseen. Tietokantojen perusteet -kurssiin nojaten taulut luotaisiin itse asiassa yleisemmällä Like-taululla, jonka taulut LikeDestination ja LikeAccomodation perisivät. Näin vältettäisiin toisto tauluissa. Työn toteutuksessa tämä tehtiin luomalla perittävä osa Like-luokkana application-hakemiston models.py-tiedostoon samaan tapaan kuin lähes kaikkien muiden tietokannan taulujen perimä Base-luokka.

Booking-taulu nimensä mukaisesti kuvastaa tehtyä varausta. Tietty varaus liittyy vain yhteen asiakkaaseen, majoituskohteeseen ja huonetyyppiin. Tämän vuoksi taulussa on kolme viiteavainta. Tauluun tarvitaan viiteavain sekä majoituskohteeseen että huonetyyppiin, sillä varauksen relaatio ainoastaan majoituskohteeseen ei sisältäisi yksiselitteistä tietoa siitä, mikä huonetyyppi varattiin. Toisaalta sama huonetyyppi voi olla useammassa majoituskohteessa, jolloin viiteavaimesta vain tauluun RoomType ei riitä.

Taulut Destination ja Accomodation kuvaavat matka- ja majoituskohteita. Kuten yllä jo todettiin, liittyy kohteisiin "tykkäyksiä". Majoituskohde on myös mahdollista varata. Jotta majoituskohteet liitettäisiin matkakohteisiin, on taulujen välillä oltava relaatio. Yhden suhde moneen -relaatio syntyy, kun tiettyyn matkakohteeseen kuuluu monta majoitusvaihtoehtoa, mutta tietty majoituskohde voi sijaita vain yhdessä matkakohteessa.

RoomType-taulu kuvastaa tarjolla olevia huonetyyppejä, jotka voivat olla tarjolla useammassa eri majoituskohteessa. Taulujen RoomType ja Accomodation välillä on monesta moneen -suhde: toisaalta huonetyyppi esiintyy monessa eri majoituskohteessa, toisaalta majoituskohteeseen liittyy monta eri tarjolla olevaa huonetyyppiä. Monesta moneen -suhde ratkaistaan tietokantarakenteessa liitostaululla, joka sisältää ainoastaan viiteavaimet kumpaankin relaation tauluun. Yllä kuvatun mukaan RoomType-taululla on relaatio myös Booking-taulun kanssa.

## Normalisointi

Tietokannan taulujen voidaan nähdä olevan niin ensimmäisessä, toisessa kuin kolmannessa normaalimuodossa. Taulujen sarakkeet täyttävät ensimmäisen normaalimuodon asettamat ehdot, ja taulujen sarakkeen "id" avulla muu tieto on yksiselitteisesti saavutettavissa. 

Toisaalta voitaisiin pohtia, olisiko taulut Client, Destination, Booking, Accomodation ja RoomType vielä normalisoitavissa. Asiakkaiden osalta sarake "username", matkakohteiden, majoituskohteiden sekä huonetyyppien osalta sarake "name" ja varausten osalta sarake "booking_number" voisi toimia vaihtoehtoisena yksilöivänä tunnisteena. Nimittäin ainoastaan yhdellä rekisteröityneellä asiakkaalla voi olla sama käyttäjätunnus, matkaan liittyvillä tietokohteilla on oltava aina kullakin taulukohtaisesti eri nimi, ja sama varausnumero ei toistu. Täydellinen normalisointi edellä mainituilta osin tosin johtaisi ongelmalliseen tietokantarakenteeseen, jossa taulujen määrä kasvaisi nopeasti suureksi. Taulujen määrän kasvaminen puolestaan johtaisi taulujen välisten kyselyiden ja raporttien luomisen hidastumiseen. Jo kuvatulla tietokantarakenteella kyselyissä on liitettävä useampia tauluja yhteen JOIN-lauseilla. Taulujen määrän kasvaminen tekisi kyselyiden ja JOIN-lauseiden käytöstä haastavamman.

Tietokantojen perusteet -kurssin materiaalissa esitettyyn normalisoinnin ja denormalisoinnin vertailuun tukeutuen voidaan päättää, että työssä käytetty tietokantarakenne ja normalisoinnin aste on sovelluksen tarpeisiin riittävä. Sovelluksen toteuttamisessa hyödytään siitä, että eri käsitteet - kuten asiakas ja varaus - ovat niihin liittyvine tietoineen yhdessä paikassa. Näin taataan myös tietokantarakenteen selkeys ja lähestyttävyys.  

## CREATE TABLE -lauseet


CREATE TABLE Client (  
	id INTEGER NOT NULL PRIMARY KEY,   
	date_created DATETIME,   
	date_modified DATETIME,   
	name VARCHAR(144) NOT NULL,   
	address VARCHAR(144) NOT NULL,   
	country VARCHAR(20) NOT NULL,   
	email VARCHAR(30) NOT NULL,   
	phone VARCHAR(20) NOT NULL,   
	username VARCHAR(20) NOT NULL,   
	password VARCHAR(10) NOT NULL   
);

CREATE TABLE LikeDestination (  
	id INTEGER NOT NULL PRIMARY KEY,   
	client_id INTEGER NOT NULL,   
	destination_id INTEGER NOT NULL,  
	date_created DATETIME,    
	FOREIGN KEY(client_id) REFERENCES Client (id),   
	FOREIGN KEY(destination_id) REFERENCES Destination (id)  
);

CREATE TABLE LikeAccomodation (  
	id INTEGER NOT NULL PRIMARY KEY,   
	client_id INTEGER NOT NULL,   
	accomodation_id INTEGER NOT NULL,  
	date_created DATETIME,     
	FOREIGN KEY(client_id) REFERENCES Client (id),   
	FOREIGN KEY(accomodation_id) REFERENCES Accomodation (id)  
);

CREATE TABLE Destination (  
	id INTEGER NOT NULL PRIMARY KEY,   
	date_created DATETIME,   
	date_modified DATETIME,   
	name VARCHAR(20) NOT NULL,   
	description VARCHAR(250) NOT NULL,   
	unavailable BOOLEAN NOT NULL  
);

CREATE TABLE Booking (  
	id INTEGER NOT NULL PRIMARY KEY,   
	roomtype_id INTEGER NOT NULL,   
	accomodation_id INTEGER NOT NULL,  
	client_id INTEGER NOT NULL,  
	date_created DATETIME,   
	date_modified DATETIME,   
	booking_number BIGINT NOT NULL,  
	approved BOOLEAN NOT NULL,   
	email_notification BOOLEAN NOT NULL,   
	phone_notification BOOLEAN NOT NULL,   
	price FLOAT NOT NULL,   
	nights INTEGER NOT NULL,    
	FOREIGN KEY(roomtype_id) REFERENCES RoomType (id),   
	FOREIGN KEY(accomodation_id) REFERENCES Accomodation (id),   
	FOREIGN KEY(client_id) REFERENCES Client (id)  
);

CREATE TABLE Accomodation (  
	id INTEGER NOT NULL PRIMARY KEY,   
        destination_id INTEGER NOT NULL,   
	date_created DATETIME,  
	date_modified DATETIME,   
	name VARCHAR(20) NOT NULL,   
	description VARCHAR(250) NOT NULL,   
	pool BOOLEAN NOT NULL,   
	spa BOOLEAN NOT NULL,   
	gym BOOLEAN NOT NULL,   
	restaurant BOOLEAN NOT NULL,  
	pricelevel FLOAT NOT NULL,   
	unavailable BOOLEAN NOT NULL,    
	FOREIGN KEY(destination_id) REFERENCES Destination (id)  
);

CREATE TABLE Association (  
	accomodation_id INTEGER,  
	roomtype_id INTEGER,  
	FOREIGN KEY(accomodation_id) REFERENCES Accomodation (id),  
	FOREIGN KEY(roomtype_id) REFERENCES RoomType (id)   
);

CREATE TABLE RoomType (  
	id INTEGER NOT NULL PRIMARY KEY,   
	date_created DATETIME,   
	date_modified DATETIME,   
	name VARCHAR(20) NOT NULL,   
	size INTEGER NOT NULL,   
	price FLOAT NOT NULL,   
	many INTEGER NOT NULL,   
	seaside_view BOOLEAN NOT NULL,   
	air_conditioned BOOLEAN NOT NULL,   
	mini_bar BOOLEAN NOT NULL,   
	tv BOOLEAN NOT NULL,   
	bath BOOLEAN NOT NULL,   
	unavailable BOOLEAN NOT NULL  
);
