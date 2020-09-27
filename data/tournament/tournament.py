# use tournament algorithm to find mvp given an list of player stats from an nba regular season
from .model import Model
import numpy as np


class Tournament:

    def __init__(self, data, model: Model):
        self.data = data
        self.model = model

    def simulate(self):
        """Simulate tournament on regular season players to get mvp"""
        keys = [d for d in self.data]

        mvp = self.simulate_helper(keys)
        print(mvp[1])

    def simulate_helper(self, keys):
        """recursive algorithm to help simulate tournament"""

        if len(keys) == 1:
            return keys
        elif len(keys) == 2:
            vector = np.concatenate(self.data[keys[0][1]], self.data[keys[1][1]])
            if self.model.evaluate(vector) > 0.5:
                return keys[0]
            else:
                return keys[1]
        else:
            return self.simulate_helper(
                [
                    self.simulate_helper(keys[:len(keys)/2]),
                    self.simulate_helper(keys[len(keys)/2:])
                ]
            )
