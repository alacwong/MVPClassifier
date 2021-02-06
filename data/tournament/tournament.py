# use tournament algorithm to find mvp given an list of player stats from an nba regular season
from .model import Model
import numpy as np
from collections import deque
from scripts.numpy_util import normalize_vector


class Tournament:

    def __init__(self, players, statistics, model: Model):
        self.player = players
        self.statistics = statistics
        self.model = model

    def simulate(self, k=5):
        """
        Simulate tournament on regular season players get
        top k mvp candidates
        """

        # iterate through all players
        q = deque([i for i in range(len(self.statistics))])

        while q:
            advance = deque([])
            if len(q) >= 2:
                i = q.popleft()
                j = q.popleft()
                stat = normalize_vector(self.statistics[i], self.statistics[j])
                pred = self.model.predict(stat)[0]
                if pred > 0.5:
                    advance.append(i)
                else:
                    advance.append(j)
            else:
                i = q.popleft()
                advance.append(i)
            if len(advance) > 1:
                q = advance
            else:
                mvp = advance.popleft()

        print(self.player[mvp])



