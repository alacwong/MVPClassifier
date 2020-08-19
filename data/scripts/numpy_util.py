import numpy as np
import pandas as pd
from typing import List, Tuple
import itertools


def normalize(x: float, y: float) -> List:
    """
    normalize values between 0 and 1
    :param x: value 1
    :param y: value 2
    :return: list of normalized x,y
    """
    if x == y:
        return 0.5
    return x / (x + y)


def normalize_vector(x: np.ndarray, y: np.ndarray) -> Tuple:
    """
    normalize vector to have range between 0 and 1
    :param x:
    :param y:
    :return:
    """
    v = []
    for i in range(len(x)):
        v.append(normalize(x[i], y[i]))
    for i in range(len(y)):
        v.append(normalize(y[i], x[i]))
    return np.array(v)


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
        vectors.append(normalize_vector(npdf[combination[0]], npdf[combination[1]]))
        vectors.append(normalize_vector(npdf[combination[1]], npdf[combination[0]]))
        labels.append(normalize(shares[combination[0]], shares[combination[1]]))
        labels.append(normalize(shares[combination[1]], shares[combination[0]]))
    return [vectors, labels]
