import abc
import numpy as np

from scripts.numpy_util import normalize_vector


class Model(abc.ABC):
    def evaluate(self, p1, p2) -> float:
        pass

    def __init__(self, engine):
        self.engine = engine


class SciKitModel(Model):

    def evaluate(self, p1, p2) -> float:
        stat = normalize_vector(p1, p2)
        stat = stat.reshape(1, len(stat))
        return self.engine.predict(stat)[0]
