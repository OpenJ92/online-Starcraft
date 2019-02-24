# this class will take in a query of the database and construct a pd.DataFrame
# or numpy.ndarray fo the queried informationself.

# Note: Be sure to start pulling in replays from previous project. ie ~/Personal_Project/Starcraft_2/sc2reader/SCReplays

class Table():
    def __init__(self):
        # make a database conntection.
        self._table = self.createTable(self.query())
        pass

    def __call__(self):
        return self._table

    def query(self, SQLstring):
        pass

    def createTable(self):
        pass
