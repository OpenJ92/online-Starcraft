from onlineDB.Transform.onlineTable import Table
from onlineDB.Database.replays.onlineModels import db
from onlineDB.Database.replays.onlineModels import Participant, User, Game, PlayerStatsEvent, UnitBornEvent, \
                         UnitTypeChangeEvent, UpgradeCompleteEvent, UnitDoneEvent, \
                         BasicCommandEvent, TargetPointCommandEvent, UnitDiedEvent, UnitInitEvent
from onlineDB.Database.FSV.onlineModels import db as FSV_db
from onlineDB.Database.FSV.onlineModels import FSV
from onlineDB.HyperSphere.resolveDirection import resolveDirection
from scipy.linalg import svd

class SVD:
    def __init__(self, participant, event_name, db_):
        self.participant = participant
        self.event_name = event_name
        self.db = db_
        self.table = Table(self.participant, event_name)
        self.tSVD = self.tSVD()
        self.FSV = self.tSVD[2][0]

    def tSVD(self):
        U, s_, VT = svd(self.table.create_agg_race_table().values)
        return U, s_, VT

    def database_inject(self):
        if self.db.session.query(FSV).filter(FSV.self_participant_id == self.participant.id):
            return False
        components_ = self.tSVD[2]
        components_shape = np.array(components_.shape)

        fsv = FSV(self_user_id = self.participant.user[0].id,
                  self_participant_id = self.participant.id,
                  game_id = self.participant.game[0].id,
                  event_name = self.event_name,
                  fsv = components_.tobytes(),
                  fsv_shape = components_shape.tobytes())

        FSV_db.session.add_all([fsv])
        FSV_db.session.commit()

    def zip_name_values(self):
        names = self.table.unique_event_names()[self.event_name]
        values = self.FSV
        return list(zip(names, values))

    def zip_name_values_race(self):
        names = self.table.event_Dictionary()[self.event_name][self.participant.playrace]
        values = self.FSV
        return list(zip(names, values))

if __name__ == "__main__":
    game = db.session.query(User)[121]
    A = [SVD(participant, "UBE", FSV_db) for participant in game.participants]
