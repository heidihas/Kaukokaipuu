from application import db
from application.models import Base

from sqlalchemy.sql import text

class RoomType(Base):
    __tablename__ = 'roomtype'
    name = db.Column(db.String(20), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    many = db.Column(db.Integer, nullable=False)
    
    seaside_view = db.Column(db.Boolean, nullable=False)
    air_conditioned = db.Column(db.Boolean, nullable=False)
    mini_bar = db.Column(db.Boolean, nullable=False)
    tv = db.Column(db.Boolean, nullable=False)
    bath = db.Column(db.Boolean, nullable=False)

    bookings = db.relationship("Booking", backref='roomtype', lazy=True)

    def __init__(self, name, size, price, many):
        self.name = name
        self.size = size
        self.price = price
        self.many = many
        self.seaside_view = False
        self.air_conditioned = False
        self.mini_bar = False
        self.tv = False
        self.bath = False
    
    @staticmethod
    def remaining_roomtypes(accomodation_id):
        stmt = text("SELECT RoomType.id, RoomType.name, RoomType.size FROM RoomType"
                    " WHERE NOT EXISTS (SELECT association.roomtype_id FROM association"
                    " WHERE association.roomtype_id = RoomType.id"
                    " AND association.accomodation_id = :accomodation)"
                    " ORDER BY RoomType.size, RoomType.name").params(accomodation=accomodation_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "size":row[2]})
        
        return response
    
    @staticmethod
    def delete_accomodations_linked(roomtype_id):
        stmt = text("DELETE FROM association"
                    " WHERE (association.roomtype_id = :roomtype)").params(roomtype=roomtype_id)
        res = db.engine.execute(stmt)
    
    @staticmethod
    def roomtypes_alpabetic():
        stmt = text("SELECT RoomType.id, RoomType.name FROM RoomType"
                    " GROUP BY RoomType.id"
                    " ORDER BY RoomType.name")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        
        return response
    