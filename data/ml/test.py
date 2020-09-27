# testing model effectiveness on all players
from scripts.generate_data import load_raw
from joblib import load

model = load('scikit-perceptron.joblib')

raw = [
    '../all_csv/' + str(x) + '.csv' for x in range(1980, 2020)
]

seasons = load_raw(raw)
for season in seasons:
    print(season, type(seasons[season]))