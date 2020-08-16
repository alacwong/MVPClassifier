import numpy as np
import pandas as pd


def generator_vector(df: pd.DataFrame) -> np.ndarrayex:
    """
    Dataset
    :param df: data of an nba mvp standing in dataframe
    :return: List of training data
    """
    shares = df['Shares']
    del df['Shares'], df['Player']
    vectors = []
    npdf = df.to_numpy()

    npdf = df3.to_numpy()
    training = []
    x = np.concatenate((npdf[0], npdf[1]))

    # def normalize(x, y):
    #     return [x / (x + y), y / [x + y]]
    #
    # for combination in list(itertools.combinations(range(len(npdf)), 2)):
    #     training.append(
    #         (
    #             np.concatenate((npdf[combination[1]], npdf[combination[1]])),
    #             np.array(normalize(shares[combination[0]], shares[combination[1]]), dtype=float)
    #         )
    #     )