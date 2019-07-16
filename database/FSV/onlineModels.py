from onlineDB.Database.FSV.createonlineDB import db
from datetime import datetime

class FSV(db.Model):
    __tablename__ = "FSV"
    
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    participant_id = db.Column(db.Integer)
    game_id = db.Column(db.Integer)
    event_name = db.Column(db.Text)
    fsv = db.Column(db.Text) # .tobytes() method on n.arrays
    fsv_shape = db.Column(db.Text) # .tobytes() method on n.arrays

db.create_all()
