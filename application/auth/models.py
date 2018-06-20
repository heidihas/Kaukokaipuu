from application import db
from application.models import Base

from sqlalchemy.sql import text

class Client(Base):

    __tablename__ = "client"

    name = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(144), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(10), nullable=False)

    bookings = db.relationship("Booking", backref='client', lazy=True)
    likes_destination = db.relationship("LikeDestination", backref='client', lazy=True)
    likes_accomodation = db.relationship("LikeAccomodation", backref='client', lazy=True)

    def __init__(self, name, address, country, email, phone, username, password):
        self.name = name
        self.address = address
        self.country = country
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password
    
    def get_id(self):
        return self.id
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def is_authenticated(self):
        return True

    def roles(self):
        if self.username == "admin":
            return ["ADMIN"]
        return ["CLIENT"]
    
    @staticmethod
    def how_many_bookings():
        stmt = text("SELECT Client.name, COUNT(Booking.id) FROM Client"
                    " LEFT JOIN Booking ON Booking.client_id = Client.id"
                    " WHERE Client.username != 'admin'"
                    " GROUP BY Client.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "count":row[1]})
        
        return response