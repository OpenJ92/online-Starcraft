from onlineDB.onlineTable import Table
from onlineDB.database.replays.onlineModels import db
from onlineDB.database.replays.onlineModels import Participant, User, Game, PlayerStatsEvent, UnitBornEvent, \
                         UnitTypeChangeEvent, UpgradeCompleteEvent, UnitDoneEvent, \
                         BasicCommandEvent, TargetPointCommandEvent, UnitDiedEvent, UnitInitEvent
from onlineDB.database.FSV.onlineModels import db as FSV_db
from onlineDB.database.FSV.onlineModels import FSV
from onlineDB.HyperSphere.resolveDirection import resolveDirection
from sklearn.decomposition import TruncatedSVD
from scipy.linalg import svd

class SVD:
    def __init__(self, participant, event_name, db_):
        self.participant = participant
        self.db = db_
        self.table = Table(self.participant, event_name)
        self.tSVD = self.tSVD()

    def tSVD(self):
        U, s_, VT = svd(self.table.create_agg_table().values)
        import pdb;pdb.set_trace()
        return 0

    def database_inject(self):
        components_ = self.tSVD.components_[:,0].tobytes()
        pass

if __name__ == "__main__":
    p = db.session.query(Participant)[20]
    pca = SVD(p, "UBE", FSV_db)
