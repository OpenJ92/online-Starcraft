# onlineTransfer.py
import shutil
import os

class Transfer():
    def __init__(self, site):
        self.site_ = site

    def run(self):
        source, destination = self.generatePaths()
        files = os.listdir(source)
        [shutil.move(source+file, destination) for file in files]

    def generatePaths(self):
        source = '/Users/jacob/Desktop/Personal_Project/Starcraft_2/onlineDB/ScrapeReplay/temporaryReplayContainer/' + self.site_ + '/'
        destination = '/Users/jacob/Desktop/Personal_Project/Starcraft_2/onlineDB/ScrapeReplay/legacyReplayContainer/' + self.site_ + '/'
        return source, destination
