# Tietokannan rakenne



<p align="center">
  <img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/kaukokaipuu_tietokantakaavio.jpg">
</p>

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
