#!/usr/bin/env python3
from onlineScrape import Scrape
from onlineInject import Inject
from onlinePull import Pull
from onlineTransfer import Transfer

sites = ['sc2r', 'ggg', 'lotv']

for site in sites:
    print(site)
    print('Scrape')
    Scrape(site).run() #Scrape content from website
    print('Inject(Pull)')
    Inject(Pull(site).run()).run() #Inject replay data into postGres .db.
    print('Transfer')
    Transfer(site).run() #Transfer replay files into legacy dir.
    print('------------')
