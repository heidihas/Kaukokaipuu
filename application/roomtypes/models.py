from application import db
from application.models import Base

from sqlalchemy.sql import text

class RoomType(Base):
    
    name = db.Column(db.String(20), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    
    seaside_view = db.Column(db.Boolean, nullable=False)
    air_conditioned = db.Column(db.Boolean, nullable=False)
    mini_bar = db.Column(db.Boolean, nullable=False)
    tv = db.Column(db.Boolean, nullable=False)
    bath = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price
        self.seaside_view = False
        self.air_conditioned = False
        self.mini_bar = False
        self.tv = False
        self.bath = False