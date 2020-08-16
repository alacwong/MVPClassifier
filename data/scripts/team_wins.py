# module for computing team wins
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
from utils.bs4_utils import get_filter, get_text


def get_add_team_df(url, df) -> pd.DataFrame:
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
    print(tm)
    print('*******')
    print(df['Tm'])
    df['Tm'].apply(lambda x: tm[x])
    return df
