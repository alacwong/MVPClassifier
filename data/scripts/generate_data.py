# script to scrape mvp data
from scripts.panda_util import get_df
import numpy as np

# ( mvps-votings, team-wins)
urls = [
    (
     'https://www.basketball-reference.com/awards/awards_' + str(x) + '.html',
     'https://www.basketball-reference.com/leagues/NBA_' + str(x) + '_standings.html'
    )
    for x in range(1980, 2020)  # include era of 3 point
]

df = get_df(('https://www.basketball-reference.com/awards/awards_2016.html','https://www.basketball-reference.com/leagues/NBA_2016_standings.html' ))
print(df)
