import numpy as np
import pandas as pd
from typing import List, Tuple
import itertools


def normalize(x: float, y: float) -> float:
    """
    normalize values between 0 and 1
    :param x: value 1
    :param y: value 2
    :return: list of normalized x,y
    """
    if x == y:
        return 0.5
    if x + y == 0:
        return 0
    return x / (x + y)


def normalize_vector(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    normalize vector to have range between 0 and 1
    :param x:
    :param y:
    :return:
    """
    v = []
    for i in range(len(x)):
        v.append(normalize(x[i], y[i]))
    return np.array(v)


# def normalize_vector(x, y):
#     v = []
#     for i in range(len(x)):
#         v.append(normalize(x[i], y[i]))
#     for i in range(len(y)):
#         v.append(normalize(x[i], y[i]))
#     return np.array(v)

def generator_vector(df: pd.DataFrame) -> List:
    """
    Dataset
    :param df: data of an nba mvp standing in dataframe
    :return: List of training data
    """
    shares = df['Share']
    players = df['Player']
    player_vs = []
    del df['Share'], df['Player']
    vectors = []
    labels = []
    npdf = df.to_numpy()

    for combination in list(itertools.combinations(range(len(npdf)), 2)):
        player_vs.append((players[combination[0]], players[combination[1]]))
        player_vs.append((players[combination[1]], players[combination[0]]))
        vectors.append(normalize_vector(npdf[combination[0]][1:], npdf[combination[1]][1:]))
        vectors.append(normalize_vector(npdf[combination[1]][1:], npdf[combination[0]][1:]))
        labels.append(normalize(shares[combination[0]], shares[combination[1]]))
        labels.append(normalize(shares[combination[1]], shares[combination[0]]))

    return [vectors, labels, player_vs]


def assign_vector(df: pd.DataFrame):
    vector_keys = []
    vector_dict = {}
    for i in range(len(df['Player'])):
        vector_keys.append((i, df['Player'][i]))
    del df['Player']
    npdf = df.to_numpy()
    for i in range(len(npdf)):
        vector_dict[vector_keys[i]] = npdf[i]
    return vector_dict


def split_data(p: float, data: List, labels: List):
    """
    Split data into
    :param labels: labels of dataset
    :param data: total dataset
    :param p: ratio of training to test
    :return:
    """
    train = []
    test = []
    train_labels = []
    test_labels = []
    for i in range(len(data)):
        x = np.random.uniform(0, 1)
        if x <= p:
            train.append(data[i])
            train_labels.append(labels[i])
        else:
            test.append(data[i])
            test_labels.append(labels[i])
    return [np.array(train), np.array(train_labels),
            np.array(test), np.array(binarize_labels(test_labels))]


def binarize_labels(labels):
    """
    set replace normalized mvp share to better player
    :param labels:
    :return:
    """
    new_labels = []
    for i in range(len(labels)):
        label = binarize(labels[i])
        new_labels.append(label)
    return new_labels


def binarize(x):
    if x >= 0.5:
        return 1
    else:
        return 0

def clean_data(df: pd.DataFrame):
    """
    Clean data to return a list of players and a list of their stats
    :param df:
    :return:
    """

    players = df['Player']
