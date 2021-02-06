import abc
import numpy as np


class Model(abc.ABC):
    def evaluate(self, sample: np.ndarray) -> float:
        pass

    def __init__(self, engine):
        self.engine = engine


class SciKitModel(Model):

    def evaluate(self, sample: np.ndarray) -> float:
        return self.engine.predict(sample)[0]
