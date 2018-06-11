from application import db
from application.models import Base

from sqlalchemy.sql import text

class Booking(Base):

    approved = db.Column(db.Boolean, nullable=False)
    email_notification = db.Column(db.Boolean, nullable=False)
    phone_notification = db.Column(db.Boolean, nullable=False)

    accomodation_id = db.Column(db.Integer, db.ForeignKey('accomodation.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    def __init__(self, accomodation_id):
        self.approved = False
        self.email_notification = False
        self.phone_notification = False
        self.accomodation_id = accomodation_id
    
    @staticmethod
    def approved_bookings(client_id, approved):
        stmt = text("SELECT Booking.id, Booking.email_notification, Booking.phone_notification, Accomodation.name, Destination.name" 
                    " FROM Booking, Accomodation, Destination"
                    " WHERE (Booking.client_id = :client AND Booking.approved = :approved)"
                    " AND Booking.accomodation_id = Accomodation.id"
                    " AND Accomodation.destination_id = Destination.id").params(client=client_id, approved=approved)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "email":row[1], "phone":row[2], "accomodation":row[3], "destination":row[4]})
        
        return response
    
    @staticmethod
    def all_bookings():
        stmt = text("SELECT Booking.id, Booking.approved, Booking.email_notification, Booking.phone_notification, Accomodation.name, Destination.name, Client.name"
                    " FROM Booking, Accomodation, Destination, Client"
                    " WHERE Booking.client_id = Client.id"
                    " AND Booking.accomodation_id = Accomodation.id"
                    " AND Accomodation.destination_id = Destination.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "approved":row[1], "email":row[2], "phone":row[3], "accomodation":row[4], "destination":row[5], "client":row[6]})
        
        return response