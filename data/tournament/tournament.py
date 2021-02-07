# use tournament algorithm to find mvp given an list of player stats from an nba regular season
from .model import Model
import numpy as np
from collections import deque
from scripts.numpy_util import normalize_vector
from .node import Node
from copy import deepcopy


class Tournament:

    def __init__(self, players, statistics, model: Model):
        self.player = players
        self.statistics = statistics
        self.model = model

    def simulate(self):
        """
        Generate binary tournament tree
        """

        # Initialize base tree
        q = deque([Node(i) for i in range(len(self.statistics))])
        advance = deque([])
        root = None

        while q or advance:
            if q:
                if len(q) > 1:
                    left = q.popleft()
                    right = q.popleft()
                    stat = normalize_vector(self.statistics[left.val], self.statistics[right.val])
                    stat = stat.reshape(1, len(stat))
                    pred = self.model.evaluate(stat)
                    if pred > 0.5:
                        advance.append(Node(left.val, left, right, pred))
                    else:
                        advance.append(Node(right.val, left, right, pred))
                else:
                    node = q.popleft()
                    advance.append(node)
            else:
                if len(advance) > 1:
                    q = advance
                    advance = deque([])
                else:
                    print('root')
                    root = advance.popleft()

        print(len(advance))
        print(f'Mvp is {self.player[root.val]}')
        return root

    def pop(self, root: Node, k):
        """
        Pop k best players from binary tournament
        :param root: binary tournament root
        :param k: number of players
        :return:
        """
        pass

        # get copy of tournament to mutate
        root_copy = deepcopy(root)
