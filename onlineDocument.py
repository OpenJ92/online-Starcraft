import re
import nltk
import gensim

class Document():
    def __init__(self, replay_path):
        self.replay_path = replay_path
        self.document = self.construct_document()

    def construct_document(self):
        self.load_replay()
    def load_replay(self):
        pass

    # we want to construct documents out of our Starcraft 2 replays as a means
    # to perform ML NLP analysis. LSTM, clustering etc...
    # We're looking to apply Word to Vec and n-gram prediction to the replays
    # Think about how to consrtuct 'words' and a grammer for these documents
    
    #https://en.wikipedia.org/wiki/Word2vec
