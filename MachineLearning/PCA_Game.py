from onlineDB.onlineTable import Table
from onlineDB.database.replays.onlineModels import db
from onlineDB.database.replays.onlineModels import Participant, User, Game, PlayerStatsEvent, UnitBornEvent, \
                         UnitTypeChangeEvent, UpgradeCompleteEvent, UnitDoneEvent, \
                         BasicCommandEvent, TargetPointCommandEvent, UnitDiedEvent, UnitInitEvent
from onlineDB.HyperSphere.resolveDirection import resolveDirection
from sklearn.decomposition import PCA

class PCA_:
    def __init__(self, participant, event_name):
        self.participant = participant
        self.table = Table(self.participant, event_name)
        self.pca = self.FSV()

    def FSV(self):
        pca = PCA(copy = False)
        return pca.fit(self.table.table.values)

if __name__ == "__main__":
    p = db.session.query(Participant)[20]
    pca = PCA_(p, "UBE")
