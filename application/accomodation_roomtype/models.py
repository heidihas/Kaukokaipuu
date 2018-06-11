from application import db

class AccomodationRoomType(db.Model):

    accomodation_id = db.Column(db.Integer, db.ForeignKey('accomodation.id'), nullable=False)
    roomtype_id = db.Column(db.Integer, db.ForeignKey('roomtype.id'), nullable=False)
    
    def __init__(self, accomodation_id, roomtype_id):
        self.accomodation_id = accomodation_id
        self.roomtype_id = roomtype_id