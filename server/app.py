from flask import Flask
from data.scripts.generate_data import scrape_players
from data.tournament.tournament import Tournament
from joblib import load

from tournament.model import SciKitModel

app = Flask(__name__)

model = load('MVPClassifier/data/ml/scikit-perceptron.joblib')
players, stats = scrape_players(2021)
t = Tournament(players, stats, SciKitModel(engine=model))
root = t.simulate()


@app.route('/')
def get_mvp():

    mvps = [str(mvp) for mvp in t.pop(root, 5)]
    return {
        'mvps': mvps
    }
