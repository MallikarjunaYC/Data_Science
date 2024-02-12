**Objective**:

The objective of the project aims to assemble the best t20 team based on players from all over the world

1. The team composition should be based on 2022 world cup performance.
2. The data should be taken from the cricinfo.com website. 

**Outcome**:

Team composition

**Tools Used**:

1. Python for data analysis
2. Beautiful soup for data scraping
3. Power BI for data visualization

**Execution**:

The links for obtaining data are - 

team - https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450

individual matches - https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/namibia-vs-sri-lanka-1st-match-first-round-group-a-1298135/full-scorecard

individual player - https://www.espncricinfo.com/cricketers/michael-van-lingen-833777

The teams link, provides a list of all matches that happened in the world cup. This list will lead to individual matches. Each individual match in turn will lead to players info.

The data is scraped from these links using Python and Beautiful Soup. 

Various data is captured like Teams name, players name, batting score, bowling information etc.

The data thus scraped is curated by eliminating duplicates, null values. The different aspects of each player, team, match is combined/linked by developing relationships to arrive at the team composition.

Finally, they are aggregated and transformed using python

and presented in Power BI to get.
