#!/bin/bash
cd /Users/jacob/Desktop/Personal_Project/Starcraft_2
source onlineDB/ONLINESTARCRAFT/bin/activate

date_of_execution="$(date)"
touch onlineDB/scrape_logs/"${date_of_execution}".txt
$(which python) onlineDB/runonlineDB.py > onlineDB/scrape_logs/"${date_of_execution}".txt

deactivate
