import numpy as np
import pandas as pd
from typing import List
import itertools


def normalize(x: float, y: float) -> List:
    """
    normalize values between 0 and 1
    :param x: value 1
    :param y: value 2
    :return: list of normalized x,y
    """
    return [x / (x + y), y / (x + y)]


def generator_vector(df: pd.DataFrame) -> List:
    """
    Dataset
    :param df: data of an nba mvp standing in dataframe
    :return: List of training data
    """
    shares = df['Share']
    del df['Share'], df['Player']
    vectors = []
    labels = []
    npdf = df.to_numpy()
    for combination in list(itertools.combinations(range(len(npdf)), 2)):
        vectors.append( np.concatenate((npdf[combination[1]], npdf[combination[1]])))
        labels.append(np.array(normalize(shares[combination[0]], shares[combination[1]]), dtype=float))
    return [vectors, labels]


