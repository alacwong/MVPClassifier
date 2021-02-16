# script to scrape mvp data
from scripts.panda_util import get_df, get_season_df
from scripts.numpy_util import generator_vector, assign_vector
import time
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import json
from utils.bs4_utils import get_filter
from scripts.panda_util import clean_regular_df


def get_data():
    """
    generate data
    :return:
    """

    start = time.time()

    for year in range(1980, 2020):
        url = (
            'https://www.basketball-reference.com/awards/awards_' + str(year) + '.html',
            'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_standings.html'
        )
        df = get_df(url)
        df.to_csv(str(year) + '.csv')

    end = time.time()
    print('Loaded  elements in %f s' % (end - start))


def get_season_data():
    """
    generate data for players among entire season
    :return:
    """

    start = time.time()
    for year in range(1980, 2020):
        url = (
            'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_per_game.html',
            'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_standings.html',
            'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_advanced.html'
        )
        df = get_season_df(url)
        df.to_csv('../all_csv/' + str(year) + '.csv')
    end = time.time()
    print('Loaded elements in %f s' % (end - start))


def load_data(files):
    data = []
    data_labels = []
    all_players = []
    for file in files:
        df = pd.read_csv(file)
        training, labels, players = generator_vector(df)
        data = data + training
        data_labels = data_labels + labels
        all_players = all_players + players
    return [data, data_labels, all_players]


def load_raw(files):
    seasons = {}
    for file in files:
        seasons[file] = assign_vector(pd.read_csv(file))
    return seasons


def scrape_players(year=2021):
    """
    Scrape players
    :return:
    """

    # In prod use config file to load year
    link = f'https://www.basketball-reference.com/leagues/NBA_{year}_totals.html'
    advanced = f'https://www.basketball-reference.com/leagues/NBA_{year}_advanced.html'
    team_summary = f'https://www.basketball-reference.com/leagues/NBA_{year}.html'

    response = get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    table_data = [t.text for t in soup.find_all('td')]
    header_data = [h.text for h in soup.find_all('th')][1:30]
    all_players = []

    win_share = {}

    # get player statistics
    for i in range(0, len(table_data), len(header_data)):
        player = {}
        for j in range(len(header_data)):
            player[header_data[j]] = table_data[i + j]
        if player['Tm'] != 'TOT':
            all_players.append(player)
            win_share[(player['Player'], player['Tm'], player['Pos'])] = player

    # get advanced stats (win-share)
    response = get(advanced)
    soup = BeautifulSoup(response.text, 'html.parser')
    advanced_header = [h.text for h in soup.find_all('th')][1:29]
    advanced_stats = [s.text for s in soup.find_all('td')]

    for i in range(0, len(advanced_stats), len(advanced_header)):
        stats = {}
        for j in range(len(advanced_header)):
            stats[advanced_header[j]] = advanced_stats[i + j]

        if stats['Tm'] != 'TOT':
            win_share[(stats['Player'], stats['Tm'], stats['Pos'])]['WS'] = stats['WS']

    # get team statistics
    response = get(team_summary)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('assets/teams.json') as f:
        tm_team = json.load(f)
    team_tm = {tm_team[tm]: tm for tm in tm_team}

    tm_pct = {}
    tm_table = list(soup.find_all('table'))
    east_func, west_func = get_filter()
    ecf = list(filter(east_func, tm_table))[0]
    wcf = list(filter(west_func, tm_table))[0]
    east = [tm_name.text for tm_name in ecf.find_all('a')]
    west = [tm_name.text for tm_name in wcf.find_all('a')]
    east_pct = [pct.text for pct in ecf.find_all('td', attrs={"data-stat": 'win_loss_pct'})]
    west_pct = [pct.text for pct in wcf.find_all('td', attrs={"data-stat": 'win_loss_pct'})]

    for i in range(len(east)):
        tm_pct[team_tm[east[i]]] = east_pct[i]

    for i in range(len(west)):
        tm_pct[team_tm[west[i]]] = west_pct[i]

    for player in all_players:
        player['Tm'] = tm_pct[player['Tm']]

    df = clean_regular_df(pd.DataFrame(all_players))
    players = list(df['Player'])
    del df['Player']
    df = df.to_numpy()
    statistics = list(df)

    print(f'Loaded {len(all_players)} player statistics from NBA year {year}')
    return players, statistics


if __name__ == "__main__":
    # get_data()
    # get_season_data()
    scrape_players()
