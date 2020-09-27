# script to scrape mvp data
from scripts.panda_util import get_df, get_season_df
from scripts.numpy_util import generator_vector
import time
import pandas as pd


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
    for file in files:
        df = pd.read_csv(file)
        training, labels = generator_vector(df)
        data = data + training
        data_labels = data_labels + labels
    return [data, data_labels]


if __name__ == "__main__":
    # get_data()
    get_season_data()
