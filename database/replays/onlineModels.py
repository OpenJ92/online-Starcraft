from onlineDB.database.replays.createonlineDB import db
from datetime import datetime

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Participant
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))

    participants = db.relationship('Participant', secondary = 'participants_users', back_populates = 'user')

    name = db.Column(db.Text)
    region = db.Column(db.Text)
    subregion = db.Column(db.Integer)

    def __repr__(self):
        return '<User (name = ' + self.name + ') >'

    def __str__(self):
        return 'user'

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Participant
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Participant(db.Model):
    __tablename__ = 'participants'

    id = db.Column(db.Integer, primary_key = True)
    game = db.relationship('Game', secondary = 'participants_games', back_populates = 'participants')
    user = db.relationship('User', secondary = 'participants_users', back_populates = 'participants')

    name = db.Column(db.Text)
    league = db.Column(db.Text)
    scaled_rating = db.Column(db.Integer)
    playrace = db.Column(db.Text)
    avg_apm = db.Column(db.Float)
    winner = db.Column(db.Boolean)

    events_PSE = db.relationship('PlayerStatsEvent', back_populates = 'participant')
    events_UBE = db.relationship('UnitBornEvent', back_populates = 'participant')
    events_UTCE = db.relationship('UnitTypeChangeEvent', back_populates = 'participant')
    events_UCE = db.relationship('UpgradeCompleteEvent', back_populates = 'participant')
    events_UIE = db.relationship('UnitInitEvent', back_populates = 'participant')
    events_UDE = db.relationship('UnitDoneEvent', back_populates = 'participant')
    events_BCE = db.relationship('BasicCommandEvent', back_populates = 'participant')
    events_TPE = db.relationship('TargetPointCommandEvent', back_populates = 'participant')
    events_UDiE = db.relationship('UnitDiedEvent', back_populates = 'participant')

    def __repr__(self):
        return '<Participant (name = ' + self.name + ') >'

    def __str__(self):
        return 'participant'

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

    def events_(self, event):
        if event == 'PSE':
            return self.events_PSE
        elif event == 'UBE':
            return self.events_UBE
        elif event == 'UTCE':
            return self.events_UTCE
        elif event == 'UCE':
            return self.events_UCE
        elif event == 'UIE':
            return self.events_UIE
        elif event == 'UDE':
            return self.events_UDE
        elif event == 'BCE':
            return self.events_BCE
        elif event == 'TPE':
            return self.events_TPE
        elif event == 'UDiE':
            return self.events_UDiE
        else:
            return None

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Game
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))

    participants = db.relationship('Participant', secondary = 'participants_games', back_populates = 'game')

    name = db.Column(db.Text)
    map = db.Column(db.Text)
    game_winner = db.Column(db.Text)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    category = db.Column(db.Text)
    expansion = db.Column(db.Text)
    time_zone = db.Column(db.Float)

    def __repr__(self):
        return '<Game (map = ' + str(self.map) + ', ' + str(self.start_time) + ') >'

    def __str__(self):
        return 'game'

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Events
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class PlayerStatsEvent(db.Model):
    __tablename__ = 'playerstatsevents'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    participant = db.relationship('Participant', back_populates = 'events_PSE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    minerals_current = db.Column(db.Float)
    vespene_current = db.Column(db.Float)
    minerals_collection_rate = db.Column(db.Float)
    vespene_collection_rate = db.Column(db.Float)
    workers_active_count = db.Column(db.Float)
    minerals_used_in_progress_army = db.Column(db.Float)
    minerals_used_in_progress_economy = db.Column(db.Float)
    minerals_used_in_progress_technology = db.Column(db.Float)
    minerals_used_in_progress = db.Column(db.Float)
    vespene_used_in_progress_army = db.Column(db.Float)
    vespene_used_in_progress_economy = db.Column(db.Float)
    vespene_used_in_progress_technology = db.Column(db.Float)
    vespene_used_in_progress = db.Column(db.Float)
    resources_used_in_progress = db.Column(db.Float)
    minerals_used_current_army = db.Column(db.Float)
    minerals_used_current_economy = db.Column(db.Float)
    minerals_used_current_technology = db.Column(db.Float)
    minerals_used_current = db.Column(db.Float)
    vespene_used_current_army = db.Column(db.Float)
    vespene_used_current_economy = db.Column(db.Float)
    vespene_used_current_technology = db.Column(db.Float)
    vespene_used_current = db.Column(db.Float)
    resources_used_current = db.Column(db.Float)
    minerals_lost_army = db.Column(db.Float)
    minerals_lost_economy = db.Column(db.Float)
    minerals_lost_technology = db.Column(db.Float)
    minerals_lost = db.Column(db.Float)
    vespene_lost_army = db.Column(db.Float)
    vespene_lost_economy = db.Column(db.Float)
    vespene_lost_technology = db.Column(db.Float)
    vespene_lost = db.Column(db.Float)
    resources_lost = db.Column(db.Float)
    minerals_killed_army = db.Column(db.Float)
    minerals_killed_economy = db.Column(db.Float)
    minerals_killed_technology = db.Column(db.Float)
    minerals_killed = db.Column(db.Float)
    vespene_killed_army = db.Column(db.Float)
    vespene_killed_economy = db.Column(db.Float)
    vespene_killed_technology = db.Column(db.Float)
    vespene_killed = db.Column(db.Float)
    resources_killed = db.Column(db.Float)
    food_used = db.Column(db.Float)
    food_made = db.Column(db.Float)
    minerals_used_active_forces = db.Column(db.Float)
    vespene_used_active_forces = db.Column(db.Float)
    ff_minerals_lost_army = db.Column(db.Float)
    ff_minerals_lost_economy = db.Column(db.Float)
    ff_minerals_lost_technology = db.Column(db.Float)
    ff_vespene_lost_army = db.Column(db.Float)
    ff_vespene_lost_economy = db.Column(db.Float)
    ff_vespene_lost_technology = db.Column(db.Float)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.participant.name + ') >'

    def column_names():
        return []

class UnitBornEvent(db.Model):
    __tablename__ = 'unitbornevents'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))

    participant = db.relationship('Participant', back_populates = 'events_UBE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    unit_type_name = db.Column(db.Text)
    loc_x = db.Column(db.Float)
    loc_y = db.Column(db.Float)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.participant.name + ') >'

    @classmethod
    def get_col_names(cls):
        return ['id', 'participant_id', 'name', 'second', 'unit_type_name', 'loc_x', 'loc_y']

#Take a closer look at this
class UnitDiedEvent(db.Model):
    __tablename__ = 'unitdiedevents'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))

    participant = db.relationship('Participant', back_populates = 'events_UDiE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    killing_unit = db.Column(db.Text)
    unit = db.Column(db.Text)
    loc_x = db.Column(db.Float)
    loc_y = db.Column(db.Float)

    def __repr__(self):
        return '<' + self.name + ' (participant = ' + self.participant.name + ') >'

    @classmethod
    def get_col_names(cls):
        return ['id', 'participant_id', 'name', 'second', 'killing_unit', 'unit', 'loc_x', 'loc_y']

class UnitTypeChangeEvent(db.Model):
    __tablename__ = 'unittypechangeevents'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))

    participant = db.relationship('Participant', back_populates = 'events_UTCE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    unit = db.Column(db.Text)
    unit_type_name = db.Column(db.Text)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.participant.name + ') >'

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

class UpgradeCompleteEvent(db.Model):
    __tablename__ = 'upgradecompleteevents'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))

    participant = db.relationship('Participant', back_populates = 'events_UCE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    upgrade_type_name = db.Column(db.Text)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.participant.name + ') >'

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

class UnitInitEvent(db.Model):
    __tablename__ = 'unitinitevent'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))

    participant = db.relationship('Participant', back_populates = 'events_UIE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    unit_type_name = db.Column(db.Text)
    loc_x = db.Column(db.Float)
    loc_y = db.Column(db.Float)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.participant.name + ') >'

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

class UnitDoneEvent(db.Model):
    __tablename__ = 'unitdoneevent'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))

    participant = db.relationship('Participant', back_populates = 'events_UDE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    unit = db.Column(db.Text)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.participant.name + ') >'

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

class BasicCommandEvent(db.Model):
    __tablename__ = 'basiccommandevent'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))

    participant = db.relationship('Participant', back_populates = 'events_BCE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    ability_name = db.Column(db.Text)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.participant.name + ') >'

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

class TargetPointCommandEvent(db.Model):
    __tablename__ = 'targetpointevent'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))

    participant = db.relationship('Participant', back_populates = 'events_TPE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    ability_name = db.Column(db.Text)
    loc_x = db.Column(db.Float)
    loc_y = db.Column(db.Float)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.participant.name + ') >'

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Join
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Participants_Games(db.Model):
    __tablename__ = 'participants_games'

    id = db.Column(db.Integer, primary_key = True)
    player_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))

class Participants_Users(db.Model):
    __tablename__ = 'participants_users'

    id = db.Column(db.Integer, primary_key = True)
    player_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

db.create_all()
