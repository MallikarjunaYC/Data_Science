This project aims to assemble a t20 team 
1. which will have players from all over the world and
2. team composition is based on 2022 world cup performance.

Thecricketers data is scraped from cricinfo.com website. 
The links are 

team - https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450


individual matches - https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/namibia-vs-sri-lanka-1st-match-first-round-group-a-1298135/full-scorecard


individual player - https://www.espncricinfo.com/cricketers/michael-van-lingen-833777


The data is scraped from these links using Python and Beautiful Soup.
The data thus scraped is curated by eliminating duplicates, null values. The diffetent aspects of each player, team, match is combined/linked by developing relationships to arrive at the team composition.

The teams link, provides a list of all matches that happened in the world cup.
This list will lead to individual matches.
Each individual match in turn will lead to players info.


Various data is captured like Teams name, players name, batting score, bowling information etc.

Finally they are aggregated and tranformed and presented in PowerBI to get. 

1. which will have players from all over the world and
2. team composition is based on 2022 world cup performance.
