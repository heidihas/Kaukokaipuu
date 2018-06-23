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

CREATE TABLE Association (  
	accomodation_id INTEGER,  
	roomtype_id INTEGER,  
	FOREIGN KEY(accomodation_id) REFERENCES Accomodation(id),  
	FOREIGN KEY(roomtype_id) REFERENCES Roomtype(id) 
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
	FOREIGN KEY(roomtype_id) REFERENCES Roomtype (id),   
	FOREIGN KEY(accomodation_id) REFERENCES Accomodation (id),   
	FOREIGN KEY(client_id) REFERENCES Client (id)  
);

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

CREATE TABLE Destination (  
	id INTEGER NOT NULL PRIMARY KEY,   
	date_created DATETIME,   
	date_modified DATETIME,   
	name VARCHAR(20) NOT NULL,   
	description VARCHAR(250) NOT NULL,   
	unavailable BOOLEAN NOT NULL  
);

CREATE TABLE LikeAccomodation (  
	id INTEGER NOT NULL PRIMARY KEY,   
	client_id INTEGER NOT NULL,   
	accomodation_id INTEGER NOT NULL,  
	date_created DATETIME,     
	FOREIGN KEY(client_id) REFERENCES Client (id),   
	FOREIGN KEY(accomodation_id) REFERENCES Accomodation (id)  
);

CREATE TABLE LikeDestination (  
	id INTEGER NOT NULL PRIMARY KEY,   
	client_id INTEGER NOT NULL,   
	destination_id INTEGER NOT NULL,  
	date_created DATETIME,    
	FOREIGN KEY(client_id) REFERENCES Client (id),   
	FOREIGN KEY(destination_id) REFERENCES Destination (id)  
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
