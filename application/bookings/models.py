from application import db
from application.models import Base

from sqlalchemy.sql import text

class Booking(Base):

    booking_number = db.Column(db.BigInteger, nullable=False)
    approved = db.Column(db.Boolean, nullable=False)
    email_notification = db.Column(db.Boolean, nullable=False)
    phone_notification = db.Column(db.Boolean, nullable=False)

    price = db.Column(db.Float, nullable=False)
    nights = db.Column(db.Integer, nullable=False)

    roomtype_id = db.Column(db.Integer, db.ForeignKey('roomtype.id'), nullable=False)
    accomodation_id = db.Column(db.Integer, db.ForeignKey('accomodation.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    def __init__(self, booking_number, price, nights, roomtype_id, accomodation_id):
        self.booking_number = booking_number
        self.approved = False
        self.email_notification = False
        self.phone_notification = False
        self.price = price
        self.nights = nights
        self.roomtype_id = roomtype_id
        self.accomodation_id = accomodation_id
    
    @staticmethod
    def approved_bookings(client_id, approved):
        stmt = text("SELECT Booking.id, Booking.booking_number, Booking.date_created, Booking.price, Booking.nights, Booking.email_notification, Booking.phone_notification, RoomType.name, RoomType.size, Accomodation.name, Destination.name" 
                    " FROM Booking, RoomType, association, Accomodation, Destination"
                    " WHERE (Booking.client_id = :client AND Booking.approved = :approved)"
                    " AND Booking.roomtype_id = RoomType.id"
                    " AND RoomType.id = association.roomtype_id"
                    " AND association.accomodation_id = Accomodation.id"
                    " AND Booking.accomodation_id = Accomodation.id"
                    " AND Accomodation.destination_id = Destination.id"
                    " ORDER BY Booking.date_created").params(client=client_id, approved=approved)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "booking_number":row[1], "date":row[2], "price":row[3], "nights":row[4], "email":row[5], "phone":row[6], "roomtype":row[7], "size":row[8], "accomodation":row[9], "destination":row[10]})
        
        return response
    
    @staticmethod
    def all_bookings():
        stmt = text("SELECT Booking.id, Booking.booking_number, Booking.date_created, Booking.approved, Booking.nights, Booking.price, Booking.email_notification, Booking.phone_notification, RoomType.name, RoomType.size, Accomodation.name, Destination.name, Client.name"
                    " FROM Booking, RoomType, association, Accomodation, Destination, Client"
                    " WHERE Booking.client_id = Client.id"
                    " AND Booking.roomtype_id = RoomType.id"
                    " AND RoomType.id = association.roomtype_id"
                    " AND association.accomodation_id = Accomodation.id"
                    " AND Booking.accomodation_id = Accomodation.id"
                    " AND Accomodation.destination_id = Destination.id"
                    " ORDER BY Booking.date_created")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "booking_number":row[1], "date":row[2], "approved":row[3], "nights":row[4], "price":row[5], "email":row[6], "phone":row[7], "roomtype":row[8], "size":row[9], "accomodation":row[10], "destination":row[11], "client":row[12]})
        
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