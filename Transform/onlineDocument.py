import re
import nltk
from createonlineDB import db
from onlineModels import Participant, User, Game, PlayerStatsEvent, UnitBornEvent, \
                         UnitTypeChangeEvent, UpgradeCompleteEvent, UnitDoneEvent, \
                         BasicCommandEvent, TargetPointCommandEvent, UnitDiedEvent, UnitInitEvent

class Document():
    def __init__(self):
        pass

    # we want to construct documents out of our Starcraft 2 replays as a means
    # to perform ML NLP analysis. LSTM, clustering etc...
    # We're looking to apply Word to Vec and n-gram prediction to the replays
    # Think about how to consrtuct 'words' and a grammer for these documents

    #https://en.wikipedia.org/wiki/Word2vec

if __name__ == "__main__":
    query = """SELECT * FROM users"""

# There should be a higherarchy of classes here to capture different kinds of
# queries. That is, if I query one replay I only need to construct a documentself.
# If I query a collection of replays from a single where we keep one or two 'features' constant,
# I should construct a 'book'. Those books should have ToC and indexes. A collection
# of books should have a library class
