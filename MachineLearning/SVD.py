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

    def tSVD(self):
        U, s_, VT = svd(self.table.create_agg_table().values)
        return U, s_, VT

    def database_inject(self):
        components_ = self.tSVD[2]
        components_shape = np.array(components_.shape)

        fsv = FSV(user_id = self.participant.user[0].id,
                  participant_id = self.participant.id,
                  game_id = self.participant.game[0].id,
                  event_name = self.event_name,
                  fsv = components_.tobytes(),
                  fsv_shape = components_shape.tobytes())

        FSV_db.session.add_all([fsv])
        FSV_db.session.commit()

if __name__ == "__main__":
    p = db.session.query(Participant)[20]
    A = SVD(p, "UBE", FSV_db)
