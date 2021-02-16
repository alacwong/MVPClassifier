from data.scripts.generate_data import scrape_players
from data.tournament.tournament import Tournament
from joblib import load

from tournament.model import SciKitModel
model = load('data/ml/scikit-perceptron.joblib')
players, stats = scrape_players(2021)
tournament = Tournament(players, stats, SciKitModel(engine=model))
root = tournament.simulate()
