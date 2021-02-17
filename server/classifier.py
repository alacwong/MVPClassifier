from data.scripts.generate_data import scrape_players
from data.tournament.tournament import Tournament
from joblib import load
from caching import r
import pickle
from datetime import date

from tournament.model import SciKitModel


def load_tournament():
    model = load('data/ml/scikit-perceptron.joblib')
    players, stats = scrape_players(2021)
    t = Tournament(players, stats, SciKitModel(engine=model))
    r.set('tournament', pickle.dumps(t))
    r.set('root', pickle.dumps(t.simulate()))
    r.set('time', str(date.today()))
