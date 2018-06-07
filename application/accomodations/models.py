from application import db
from application.models import Base

class Accomodation(Base):
    
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    
    rating = db.Column(db.Integer, nullable=False)

    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'), nullable=False)
    
    def __init__(self, name, description, destination_id):
        self.name = name
        self.description = description
        self.rating = 0
        self.destination_id = destination_id
