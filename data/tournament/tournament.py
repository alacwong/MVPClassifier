# use tournament algorithm to find mvp given an list of player stats from an nba regular season
from .model import Model
from collections import deque
from scripts.numpy_util import normalize_vector
from .node import Node
from copy import deepcopy
import random


class Tournament:

    def __init__(self, players, statistics, model: Model):
        self.player = players
        self.statistics = statistics
        self.model = model

    def shuffle(self, seed):
        """
        Shuffle array
        :return:
        """
        random.Random(seed).shuffle(self.player)
        random.Random(seed).shuffle(self.statistics)

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
                    pred = self.model.evaluate(self.statistics[left.val], self.statistics[right.val])
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
                    root = advance.popleft()

        print(f'Mvp is {self.player[root.val]}')
        return root

    def display_shallow(self, node):
        if node.left:
            left = f'Left: {self.player[node.left.val]}'
        else:
            left = ''

        if node.right:
            right = f'Right {self.player[node.right.val]}'
        else:
            right = ''

        return f'Node: {self.player[node.val]} {left} {right}'

    def pop(self, root: Node, k):
        """
        Pop k best players from binary tournament
        :param root: binary tournament root
        :param k: number of players
        :return:
        """

        # get copy of tournament to mutate
        root_copy = deepcopy(root)

        # list of k best players
        mvps = [root.val]

        while k - 1:

            # remove
            current = root_copy.base
            parent = current.parent
            if current.val == parent.left.val:
                parent.left = None
            else:
                parent.right = None

            current = parent

            while current:
                # No Children
                if current.left is None and current.right is None:
                    parent = current.parent
                    if parent.left.val == current.val:
                        parent.left = None
                        parent.base = parent.right
                    else:
                        parent.right = None
                        parent.base = parent.left

                # Left child only
                elif current.left is None:
                    current.val = current.right.val
                    current.base = current.right.base

                # Right child only
                elif current.right is None:
                    current.val = current.left.val
                    current.base = current.left.base

                # Both children are available
                else:
                    pred = self.model.evaluate(self.statistics[current.left.val], self.statistics[current.right.val])
                    if pred > 0.5:
                        current.val = current.left.val
                        current.base = current.left.base
                    else:
                        current.val = current.right.val
                        current.base = current.right.base

                    if current.parent is None:
                        mvps.append(current.val)
                        root_copy = current

                current = current.parent

            k -= 1

        return [self.player[mvp] for mvp in mvps]

    def display_tournament(self, root):
        """
        Display players
        USe bfs algorithm
        :return:
        """
        pass
