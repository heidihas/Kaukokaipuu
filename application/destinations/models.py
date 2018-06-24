from application import db
from application.models import Base

from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError

class Destination(Base):
    
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(250), nullable=False)

    unavailable = db.Column(db.Boolean, nullable=False)

    accomodations = db.relationship("Accomodation", backref='destination', lazy=True)
    likes_destination = db.relationship("LikeDestination", backref='destination', lazy=True)
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.unavailable = False

    @staticmethod
    def destinations_in_order():
        stmt = text("SELECT Destination.id, Destination.name, Destination.unavailable, COUNT(LikeDestination.id) AS likes FROM Destination"
                    " LEFT JOIN LikeDestination ON Destination.id = LikeDestination.destination_id"
                    " GROUP BY Destination.id"
                    " ORDER BY likes DESC")
        try:
            res = db.engine.execute(stmt)

            response = []
            for row in res:
                response.append({"id":row[0], "name":row[1], "unavailable":row[2], "likes":row[3]})
        except SQLAlchemyError:
            db.session.rollback()
            raise
        
        return response
    
    @staticmethod
    def destinations_alphabetic():
        stmt = text("SELECT Destination.id, Destination.name, Destination.unavailable FROM Destination"
                    " GROUP BY Destination.id"
                    " ORDER BY Destination.name")
        try:
            res = db.engine.execute(stmt)

            response = []
            for row in res:
                response.append({"id":row[0], "name":row[1], "unavailable":row[2]})
        except SQLAlchemyError:
            db.session.rollback()
            raise
        
        return response

    @staticmethod
    def how_many_bookings(destination_id):
        stmt = text("SELECT COUNT(Booking.id) FROM Accomodation"
                    " LEFT JOIN Booking ON Accomodation.id = Booking.accomodation_id"
                    " WHERE Accomodation.destination_id = :destination").params(destination=destination_id)
        try:
            count = db.engine.execute(stmt).scalar()
        except SQLAlchemyError:
            db.session.rollback()
            raise
        
        return count
    
    @staticmethod
    def how_many_bookings_all():
        stmt = text("SELECT Destination.name, COUNT(Booking.id) AS count FROM Destination"
                    " LEFT JOIN Accomodation ON Destination.id = Accomodation.destination_id"
                    " INNER JOIN Booking ON Accomodation.id = Booking.accomodation_id"
                    " GROUP BY Destination.id"
                    " ORDER BY count DESC, Destination.name ASC")
        try:
            res = db.engine.execute(stmt)

            response = []
            for row in res:
                response.append({"name":row[0], "count":row[1]})
        except SQLAlchemyError:
            db.session.rollback()
            raise
        
        return response