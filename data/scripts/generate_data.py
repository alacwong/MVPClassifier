# script to scrape mvp data
from scripts.panda_util import get_df
from scripts.numpy_util import generator_vector
import time
import numpy as np

def get_data():
    # ( mvps-votings, team-wins)
    urls = [
        (
            'https://www.basketball-reference.com/awards/awards_' + str(x) + '.html',
            'https://www.basketball-reference.com/leagues/NBA_' + str(x) + '_standings.html'
        )
        for x in range(1980, 2020)  # include era of 3 point
    ]
    data = []
    data_labels = []

    start = time.time()

    for url in urls:
        df = get_df(url)
        training, labels = generator_vector(df)
        data = data + training
        data_labels = data_labels + labels

    data = np.array(data)
    data_labels = np.array(data_labels)
    end = time.time()
    print('Loaded %d elements in %f s' % (len(data), end - start))
    return [data, data_labels]