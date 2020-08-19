# script to scrape mvp data
from scripts.panda_util import get_df
from scripts.numpy_util import generator_vector
import time
import numpy as np
from typing import List


def get_data(urls):
    """
    generate data
    :return:
    """
    data = []
    data_labels = []

    start = time.time()

    for url in urls:
        df = get_df(url)
        training, labels = generator_vector(df)
        data = data + training
        data_labels = data_labels + labels

    end = time.time()
    print('Loaded %d elements in %f s' % (len(data), end - start))
    return [data, data_labels]
