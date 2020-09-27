import abc
import numpy as np


class Model(abc.ABC):
    def evaluate(self, sample: np.ndarray) -> float:
        pass
