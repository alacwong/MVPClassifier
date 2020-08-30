# script to scrape mvp data
from scripts.panda_util import get_df
from scripts.numpy_util import generator_vector
import time
import pandas as pd
import numpy as np
from typing import List
import psycopg2


def get_data():
    """
    generate data
    :return:
    """

    start = time.time()

    for x in range(1980, 2020):
        url = (
            'https://www.basketball-reference.com/awards/awards_' + str(x) + '.html',
            'https://www.basketball-reference.com/leagues/NBA_' + str(x) + '_standings.html'
        )
        df = get_df(url)
        df.to_csv(str(x) + '.csv')

    end = time.time()
    print('Loaded  elements in %f s' % (end - start))


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
    get_data()

# if __name__ == "__main__":
#     url_data = [
#         (
#             'https://www.basketball-reference.com/awards/awards_' + str(x) + '.html',
#             'https://www.basketball-reference.com/leagues/NBA_' + str(x) + '_standings.html'
#         )
#         for x in range(1980, 2020)  # include era of 3 point
#     ]
#     # data = get_df(url_data)
#     # add to postgresql database
#
#     # connect to postgres
#     connection = psycopg2.connect(
#         user="dbuser",
#         password="password",
#         host="localhost",
#         port="5432",
#         database="training"
#     )
#     print(connection.get_dsn_parameters())
#     cur = connection.cursor()
#     sql = """CREATE TABLE(""" + """);"""
#
#
#
#     cur.execute(
#         sql
#     )
#     connection.commit()
#
#     cur.execute("""SELECT table_name FROM information_schema.tables
#            WHERE table_schema = 'public'""")
#     for table in cur.fetchall():
#         print(table)
