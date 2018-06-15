from application import db
from application.models import Base

from sqlalchemy.sql import text

class Destination(Base):
    
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    
    rating = db.Column(db.Integer, nullable=False)

    accomodations = db.relationship("Accomodation", backref='destination', lazy=True)
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.rating = 0
    
    @staticmethod
    def destinations_in_order():
        stmt = text("SELECT Destination.id, Destination.name, Destination.rating FROM Destination"
                    " GROUP BY Destination.id"
                    " ORDER BY Destination.rating DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "rating":row[2]})
        
        return response
    
    @staticmethod
    def destinations_alphabetic():
        stmt = text("SELECT Destination.id, Destination.name FROM Destination"
                    " GROUP BY Destination.id"
                    " ORDER BY Destination.name")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        
        return response
