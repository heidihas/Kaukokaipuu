from application import db
from application.models import Base

class Destination(Base):
    
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    
    rating = db.Column(db.Integer, nullable=False)

    accomodations = db.relationship("Accomodation", backref='destination', lazy=True)
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.rating = 0
