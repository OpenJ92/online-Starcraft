# onlineScrape.py
#!/usr/bin/env python

import requests
import bs4
import os
import urllib
import wget

# ------ ------ lotv.spawningtool.com
# Example:
#       https://lotv.spawningtool.com/45325/download

# ------ ------ gggreplays.com
# Example:
#       https://gggreplays.com/matches/222154/replay

class Scrape():
    def __init__(self, website):
        self.website_ = website

    def dictMeta(self):
        return {'ggg': {'link': 'https://gggreplays.com/matches/',
                        'directorylink' : '/Users/jacob/Desktop/Personal_Project/Starcraft_2/onlineDB/scrapeMetaData/ggg.txt',
                        'downloadLink': '/replay'},
                'lotv': {'link': 'https://lotv.spawningtool.com/',
                        'directorylink' : '/Users/jacob/Desktop/Personal_Project/Starcraft_2/onlineDB/scrapeMetaData/lotv.txt',
                       'downloadLink' : '/download'},
                'sc2r': {'link': 'http://sc2replaystats.com/',
                         'directorylink' : '/Users/jacob/Desktop/Personal_Project/Starcraft_2/onlineDB/scrapeMetaData/sc2r.txt',
                         'downloadLink' : 'download/'}}

    def accesslastKnownFileLocation(self):
        return open(self.dictMeta()[self.website_]['directorylink'], 'r').read()

    def writelastKnownFileLocation(self, newlastKnownLocation):
        f = open(self.dictMeta()[self.website_]['directorylink'], 'w')
        f.write(str(newlastKnownLocation))

    def downloadLink(self, currentLocation):
        if self.website_ in ['ggg', 'lotv']:
            return self.dictMeta()[self.website_]['link'] + str(currentLocation) + self.dictMeta()[self.website_]['downloadLink']
        elif self.website_ in ['sc2r']:
            return self.dictMeta()[self.website_]['link'] + self.dictMeta()[self.website_]['downloadLink'] + str(currentLocation)

    def run(self):
        exp = False
        currentLocation = int(self.accesslastKnownFileLocation())
        currentLocation_ = int(self.accesslastKnownFileLocation())
        while not exp:
            try:
                local_filename, headers = urllib.request.urlretrieve(self.downloadLink(currentLocation),
                                                                     filename = '/Users/jacob/Desktop/Personal_Project/Starcraft_2/onlineDB/temporaryReplayContainer/' + self.website_ + '/' + str(currentLocation) + '.SC2Replay')
                # wget.download(self.downloadLink(currentLocation),'/Users/jacob/Desktop/Personal_Project/Starcraft_2/onlineDB/temporaryReplayContainer/' + self.website_ + '/' + str(currentLocation) + '.SC2Replay')
                currentLocation += 1
                if currentLocation - currentLocation_ > 50:
                    exp = True
            except Exception as e:
                exp = True
                currentLocation += 1
                print(e)
        self.writelastKnownFileLocation(currentLocation)
