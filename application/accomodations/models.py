from application import db
from application.models import Base

from sqlalchemy.sql import text

class Accomodation(Base):
    
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    
    rating = db.Column(db.Integer, nullable=False)

    pool = db.Column(db.Boolean, nullable=False)
    spa = db.Column(db.Boolean, nullable=False)
    gym = db.Column(db.Boolean, nullable=False)
    restaurant = db.Column(db.Boolean, nullable=False)

    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'), nullable=False)
    bookings = db.relationship("Booking", backref='accomodation', lazy=True)
    
    def __init__(self, name, description, destination_id):
        self.name = name
        self.description = description
        self.rating = 0
        self.pool = False
        self.spa = False
        self.gym = False
        self.restaurant = False
        self.destination_id = destination_id
    
    @staticmethod
    def accomodations_in_order(destination_id):
        stmt = text("SELECT Accomodation.id, Accomodation.name, Accomodation.rating FROM Accomodation"
                    " WHERE (Accomodation.destination_id = :destination)"
                    " GROUP BY Accomodation.id"
                    " ORDER BY Accomodation.rating DESC").params(destination=destination_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "rating":row[2]})
        
        return response
