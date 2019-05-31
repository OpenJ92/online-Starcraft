#!/usr/bin/env python3
from onlineScrape import Scrape
from onlineInject import Inject
from onlinePull import Pull
from onlineTransfer import Transfer

sites = [ 'ggg', 'lotv']

for site in sites:
    Scrape(site).run() #Scrape content from website
    Inject(Pull(site).run()).run() #Inject replay data into postGres .db.
    Transfer(site).run() #Transfer replay files into legacy dir.
