from bs4 import BeautifulSoup
import pandas as pd
from requests import get
from utils.bs4_utils import get_text, get_filter, link
from typing import Tuple


def get_mvp_df(url) -> pd.DataFrame:
    """
    parse url for mvp data
    :param url: url to mvp stats
    :return: mvp data as dataframe
    """
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = list(soup.find_all('table'))
    columns = list(map(get_text,
                       tables[0].find_all('th', attrs={'scope': 'col'})))
    columns.remove('Rank')
    tags = link(tables[0].find_all('td'))
    player_stats = list(map(get_text, tags))
    mvp_candidates = []
    for i in range(0, len(player_stats), len(columns)):
        row = player_stats[i: i + len(columns)]
        mvp_candidate = {columns[j]: row[j] for j in range(len(row))}
        if mvp_candidate['Tm'] != 'TOT':
            mvp_candidates.append(mvp_candidate)
    df = pd.DataFrame(mvp_candidates)
    del df['G'], df['Pts Won'], df['Pts Max'], df['First'], df['Age'], df['WS/48']
    return df


def add_team_df(url: str, df: pd.DataFrame) -> pd.DataFrame:
    """
    Update dataframe with data from team wins
    :param df: dataframe of other data
    :param url of mvp votings for an nba season
    :return: data frame
    """
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = list(soup.find_all('table'))
    east_func, west_func = get_filter()
    east = list(filter(east_func, tables))[0]
    west = list(filter(west_func, tables))[0]
    tm_pct = list(map(get_text, east.find_all('td', attrs={"data-stat": 'win_loss_pct'}))) + \
             list(map(get_text, west.find_all('td', attrs={"data-stat": 'win_loss_pct'})))
    tm_nm = list(east.find_all('a')) + list(west.find_all('a'))
    tm = {tm_nm[i]['href']: tm_pct[i] for i in range(len(tm_nm))}
    df['Tm'] = df['Tm'].apply(lambda x: tm[x])
    return df


def to_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """
    clean df and set to numeric
    :param df:
    :return:
    """
    df = clean_df(df)
    for col in df:
        df[col] = pd.to_numeric(df[col], errors='ignore')
    return df


def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    remove empty columns and set empty cells to '0'
    :param df:
    :return:
    """
    for col in df:
        count = 0
        for i in range(len(df[col])):
            if df[col][i] == '':
                df.loc[i, col] = '0'
                count += 1
        if count == len(df[col]):
            del df[col]
    return df


def get_df(urls: Tuple) -> pd.DataFrame:
    """
    get fully cleaned df
    :param urls:
    :return:
    """
    mvp, wins = urls
    df = get_mvp_df(mvp)
    df = add_team_df(wins, df)
    df = to_numeric(df)
    return df


def get_regular_df(url):
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    header_str = "Player	Pos	Age	Tm	G	GS	MP	FG	FGA	FG%	3P	3PA	3P%	2P	2PA	2P%\teFG%\tFT	FTA	FT%	ORB	DRB	TRB	" \
                 "AST	STL	BLK	TOV	PF	PTS "

    # table headers for each stat
    headers = [header.strip() for header in header_str.split('\t')]

    table = soup.find_all('td')
    table_data = [t for t in table]  # convert table matrix to list

    players = []

    for i in range(0, len(table_data), len(headers)):
        row = table_data[i: i + len(headers)]
        player = {headers[i]: row[i].text for i in range(len(headers))}
        try:
            tm = row[3].a['href']
            player['Tm'] = tm
            players.append(player)
        except TypeError:
            continue

    return pd.DataFrame(players)


def get_win_share(url, df: pd.DataFrame) -> pd.DataFrame:
    """Get win share of year"""
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    table_data = list(tables)
    headers = table_data[0].find_all('th', attrs={'scope': 'col'})
    headers = [h.text for h in headers]
    headers.remove('Rk')
    stats = soup.find_all('td')
    table_stats = [stat.text for stat in stats]
    players = []
    for i in range(0, len(table_stats), len(headers)):
        s = table_stats[i: i + len(headers)]
        players.append({headers[i]: s[i] for i in range(len(s))})
    df['WS'] = pd.DataFrame(players)[['WS']]
    return df


def clean_regular_df(df: pd.DataFrame):
    cleaned_headers = ['Player', 'Tm', 'MP', 'PTS', 'TRB', 'AST', 'STL', 'BLK', 'FG%', '3P%', 'FT%', 'WS']
    for col in df:
        if col not in cleaned_headers:
            del df[col]
    df = df[cleaned_headers]
    return to_numeric(df)


def get_season_df(urls: Tuple):
    per_game, team_wins, advanced = urls
    regular_season = get_regular_df(per_game)
    df = add_team_df(team_wins, regular_season)
    df = get_win_share(advanced, df)
    return clean_regular_df(df)
