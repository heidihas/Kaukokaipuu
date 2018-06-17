from application import db
from application.models import Base

from sqlalchemy.sql import text

class Booking(Base):

    booking_number = db.Column(db.BigInteger, nullable=False)
    approved = db.Column(db.Boolean, nullable=False)
    email_notification = db.Column(db.Boolean, nullable=False)
    phone_notification = db.Column(db.Boolean, nullable=False)

    roomtype_id = db.Column(db.Integer, db.ForeignKey('roomtype.id'), nullable=False)
    accomodation_id = db.Column(db.Integer, db.ForeignKey('accomodation.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    def __init__(self, booking_number, roomtype_id, accomodation_id):
        self.booking_number = booking_number
        self.approved = False
        self.email_notification = False
        self.phone_notification = False
        self.roomtype_id = roomtype_id
        self.accomodation_id = accomodation_id
    
    @staticmethod
    def approved_bookings(client_id, approved):
        stmt = text("SELECT Booking.id, Booking.booking_number, Booking.date_created, Booking.email_notification, Booking.phone_notification, RoomType.name, RoomType.size, RoomType.price, Accomodation.name, Destination.name" 
                    " FROM Booking, RoomType, association, Accomodation, Destination"
                    " WHERE (Booking.client_id = :client AND Booking.approved = :approved)"
                    " AND Booking.roomtype_id = RoomType.id"
                    " AND RoomType.id = association.roomtype_id"
                    " AND association.accomodation_id = Accomodation.id"
                    " AND Booking.accomodation_id = Accomodation.id"
                    " AND Accomodation.destination_id = Destination.id"
                    " GROUP BY Booking.id, RoomType.name"
                    " ORDER BY Booking.date_created").params(client=client_id, approved=approved)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "booking_number":row[1], "date":row[2], "email":row[3], "phone":row[4], "roomtype":row[5], "size":row[6], "price":row[7], "accomodation":row[8], "destination":row[9]})
        
        return response
    
    @staticmethod
    def all_bookings():
        stmt = text("SELECT Booking.id, Booking.booking_number, Booking.date_created, Booking.approved, Booking.email_notification, Booking.phone_notification, RoomType.name, RoomType.size, RoomType.price, Accomodation.name, Destination.name, Client.name"
                    " FROM Booking, RoomType, association, Accomodation, Destination, Client"
                    " WHERE Booking.client_id = Client.id"
                    " AND Booking.roomtype_id = RoomType.id"
                    " AND RoomType.id = association.roomtype_id"
                    " AND association.accomodation_id = Accomodation.id"
                    " AND Booking.accomodation_id = Accomodation.id"
                    " AND Accomodation.destination_id = Destination.id"
                    " GROUP BY Booking.id, RoomType.name"
                    " ORDER BY Booking.date_created")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "booking_number":row[1], "date":row[2], "approved":row[3], "email":row[4], "phone":row[5], "roomtype":row[6], "size":row[7], "price":row[8], "accomodation":row[9], "destination":row[10], "client":row[11]})
        
        return response

    @staticmethod
    def booking_number_exists(booking_number):
        stmt = text("SELECT COUNT(*) FROM Booking"
                    " WHERE Booking.booking_number = :booking").params(booking=booking_number)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"count":row[0]})
        
        return response