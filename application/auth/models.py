from application import db
from application.models import Base

class Client(Base):

    __tablename__ = "client"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(10), nullable=False)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
    
    def get_id(self):
        return self.id
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def is_authenticated(self):
        return True