# module for gathering mvp data
from bs4 import BeautifulSoup
import pandas as pd
from requests import get
from utils.bs4_utils import get_text


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
    player_stats = list(map(get_text, tables[0].find_all('td')))
    mvp_candidates = []
    for i in range(0, len(player_stats), len(columns)):
        row = player_stats[i: i + len(columns)]
        mvp_candidate = {columns[j]: row[j] for j in range(len(row))}

        mvp_candidates.append(mvp_candidate)
    df = pd.DataFrame(mvp_candidates)
    del df['G'], df['Pts Won'], df['Pts Max'], df['First'], df['Age'], df['WS/48']
    return df
