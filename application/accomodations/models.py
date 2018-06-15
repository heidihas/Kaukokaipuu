from application import db
from application.models import Base

from sqlalchemy.sql import text

class Accomodation(Base):
    __tablename__ = 'accomodation'
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    
    rating = db.Column(db.Integer, nullable=False)

    pool = db.Column(db.Boolean, nullable=False)
    spa = db.Column(db.Boolean, nullable=False)
    gym = db.Column(db.Boolean, nullable=False)
    restaurant = db.Column(db.Boolean, nullable=False)

    association_table = db.Table('association', Base.metadata,
    db.Column('accomodation_id', db.Integer, db.ForeignKey('accomodation.id')),
    db.Column('roomtype_id', db.Integer, db.ForeignKey('roomtype.id')))

    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'), nullable=False)
    children = db.relationship("RoomType", secondary=association_table, backref="parents")
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
    
    @staticmethod
    def children_in_order(accomodation_id):
        stmt = text("SELECT RoomType.id, RoomType.name, RoomType.size, RoomType.price, RoomType.many, RoomType.seaside_view, RoomType.air_conditioned, RoomType.mini_bar, RoomType.tv, RoomType.bath, COUNT(Booking.id) FROM RoomType, association, Accomodation"
                    " LEFT JOIN Booking ON Booking.roomtype_id = RoomType.id"
                    " WHERE RoomType.id = association.roomtype_id"
                    " AND association.accomodation_id = :accomodation"
                    " GROUP BY RoomType.id"
                    " ORDER BY RoomType.size, RoomType.price").params(accomodation=accomodation_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "size":row[2], "price":row[3], "many":row[4], "seaside_view":row[5], "air_conditioned":row[6], "mini_bar":row[7], "tv":row[8], "bath":row[9], "booked":row[10]})
        
        return response

    @staticmethod
    def accomodations_alphabetic():
        stmt = text("SELECT Accomodation.id, Accomodation.name, Accomodation.destination_id FROM Accomodation"
                    " GROUP BY Accomodation.id"
                    " ORDER BY Accomodation.name")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "destination_id":row[2]})
        
        return response

    @staticmethod
    def delete_roomtypes_linked(accomodation_id):
        stmt = text("DELETE FROM association"
                    " WHERE (association.accomodation_id = :accomodation)").params(accomodation=accomodation_id)
        res = db.engine.execute(stmt)
    
    @staticmethod
    def delete_roomtypes_one(accomodation_id, roomtype_id):
        stmt = text("DELETE FROM association"
                    " WHERE (association.accomodation_id = :accomodation"
                    " AND association.roomtype_id = :roomtype)").params(accomodation=accomodation_id, roomtype=roomtype_id)
        res = db.engine.execute(stmt)
    
    @staticmethod
    def how_many_bookings_roomtype(accomodation_id):
        stmt = text("SELECT RoomType.id, COUNT(Booking.id) FROM RoomType"
                    " LEFT JOIN Booking ON Booking.roomtype_id = RoomType.id"
                    " WHERE Booking.accomodation_id = :accomodation"
                    " GROUP BY RoomType.id"
                    " ORDER BY RoomType.size, RoomType.name").params(accomodation=accomodation_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"roomtype":row[0], "count":row[1]})
        
        return response