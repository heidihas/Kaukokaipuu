from application import db
from application.models import Like

from sqlalchemy.sql import text

class LikeDestination(Like):

    __tablename__ = 'likedestination'
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'), nullable=False)

    def __init__(self, client_id, destination_id):
        self.client_id = client_id
        self.destination_id = destination_id
    
    @staticmethod
    def how_many_likes_destination(destination_id):
        stmt = text("SELECT COUNT(LikeDestination.id) FROM LikeDestination"
                    " WHERE LikeDestination.destination_id = :destination").params(destination=destination_id)
        count = db.engine.execute(stmt).scalar()

        return count
    
    @staticmethod
    def has_liked(client_id, destination_id):
        stmt = text("SELECT COUNT(LikeDestination.id) FROM LikeDestination"
                    " WHERE LikeDestination.client_id = :client"
                    " AND LikeDestination.destination_id = :destination").params(client=client_id, destination=destination_id)
        count = db.engine.execute(stmt).scalar()

        return count


class LikeAccomodation(Like):

    __tablename__ = 'likeaccomodation'
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    accomodation_id = db.Column(db.Integer, db.ForeignKey('accomodation.id'), nullable=False)

    def __init__(self, client_id, accomodation_id):
        self.client_id = client_id
        self.accomodation_id = accomodation_id
    
    @staticmethod
    def how_many_likes_accomodation(accomodation_id):
        stmt = text("SELECT COUNT(LikeAccomodation.id) FROM LikeAccomodation"
                    " WHERE LikeAccomodation.accomodation_id = :accomodation").params(accomodation=accomodation_id)
        count = db.engine.execute(stmt).scalar()

        return count
    
    @staticmethod
    def has_liked(client_id, accomodation_id):
        stmt = text("SELECT COUNT(LikeAccomodation.id) FROM LikeAccomodation"
                    " WHERE LikeAccomodation.client_id = :client"
                    " AND LikeAccomodation.accomodation_id = :accomodation").params(client=client_id, accomodation=accomodation_id)
        count = db.engine.execute(stmt).scalar()

        return count