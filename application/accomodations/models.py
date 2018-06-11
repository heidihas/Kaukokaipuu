from application import db
from application.models import Base

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
