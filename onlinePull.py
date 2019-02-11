# onlinePull.py
#
import os
import sc2reader
from sc2reader.engine.plugins import SelectionTracker, APMTracker
sc2reader.engine.register_plugin(SelectionTracker())
sc2reader.engine.register_plugin(APMTracker())


class Pull():
    def __init__(self, site):
        self.site_ = site

    def run(self):
        return self.pull()

    def pull(self):
        files = os.listdir('/Users/jacob/Desktop/Personal_Project/Starcraft_2/onlineDB/temporaryReplayContainer/' + self.site_)
        replay_list = []
        for file in files:
            try:
                replay_list.append(sc2reader.load_replay('/Users/jacob/Desktop/Personal_Project/Starcraft_2/onlineDB/temporaryReplayContainer/' + self.site_ + '/' + file))
            except Exception as e:
                pass
        print(replay_list)
        return replay_list
