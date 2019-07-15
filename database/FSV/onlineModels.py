from onlineDB.database.FSV.createonlineDB import db
from datetime import datetime

class FSV(db.Model):
    __tablename__ = "FSV"
    
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    participant_id = db.Column(db.Integer)
    game_id = db.Column(db.Integer)
    fsv = db.Column(db.Text)

db.create_all()
