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
