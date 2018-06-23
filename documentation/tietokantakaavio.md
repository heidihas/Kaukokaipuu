# Tietokannan rakenne



<p align="center">
  <img src="https://github.com/heidihas/Kaukokaipuu/blob/master/documentation/Pictures/kaukokaipuu_tietokantakaavio.jpg">
</p>

## CREATE TABLE -lauseet

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
	FOREIGN KEY(destination_id) REFERENCES Destination(id)  
);

CREATE TABLE association (
	accomodation_id INTEGER, 
	roomtype_id INTEGER, 
	FOREIGN KEY(accomodation_id) REFERENCES accomodation (id), 
	FOREIGN KEY(roomtype_id) REFERENCES roomtype (id)
);
CREATE TABLE booking (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	booking_number BIGINT NOT NULL, 
	approved BOOLEAN NOT NULL, 
	email_notification BOOLEAN NOT NULL, 
	phone_notification BOOLEAN NOT NULL, 
	price FLOAT NOT NULL, 
	nights INTEGER NOT NULL, 
	roomtype_id INTEGER NOT NULL, 
	accomodation_id INTEGER NOT NULL, 
	client_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (approved IN (0, 1)), 
	CHECK (email_notification IN (0, 1)), 
	CHECK (phone_notification IN (0, 1)), 
	FOREIGN KEY(roomtype_id) REFERENCES roomtype (id), 
	FOREIGN KEY(accomodation_id) REFERENCES accomodation (id), 
	FOREIGN KEY(client_id) REFERENCES client (id)
);
CREATE TABLE client (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	address VARCHAR(144) NOT NULL, 
	country VARCHAR(20) NOT NULL, 
	email VARCHAR(30) NOT NULL, 
	phone VARCHAR(20) NOT NULL, 
	username VARCHAR(20) NOT NULL, 
	password VARCHAR(10) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE destination (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(20) NOT NULL, 
	description VARCHAR(250) NOT NULL, 
	unavailable BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (unavailable IN (0, 1))
);
CREATE TABLE likeaccomodation (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	client_id INTEGER NOT NULL, 
	accomodation_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(client_id) REFERENCES client (id), 
	FOREIGN KEY(accomodation_id) REFERENCES accomodation (id)
);
CREATE TABLE likedestination (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	client_id INTEGER NOT NULL, 
	destination_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(client_id) REFERENCES client (id), 
	FOREIGN KEY(destination_id) REFERENCES destination (id)
);
CREATE TABLE roomtype (
	id INTEGER NOT NULL, 
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
	unavailable BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (seaside_view IN (0, 1)), 
	CHECK (air_conditioned IN (0, 1)), 
	CHECK (mini_bar IN (0, 1)), 
	CHECK (tv IN (0, 1)), 
	CHECK (bath IN (0, 1)), 
	CHECK (unavailable IN (0, 1))
);
