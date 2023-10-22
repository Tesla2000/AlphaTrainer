from itertools import compress
from typing import Optional

import numpy as np
from sklearn.tree import DecisionTreeClassifier

from PySplendor.Game import n_moves


def train(x, y) -> DecisionTreeClassifier:
    clf = DecisionTreeClassifier()
    clf.fit(x, y)
    return clf


def train_to_predict_win(data: np.array) -> DecisionTreeClassifier:
    y = data[:, 0]
    x = data[:, 1:]
    return train(x, y)


def train_to_predict_move(data: np.array) -> Optional[DecisionTreeClassifier]:
    y = np.array(tuple(compress(data[:, -1], data[:, 0])))
    x = np.array(tuple(compress(data[:, 1:-1], data[:, 0])))
    if len(np.unique(y)) != n_moves:
        return
    return train(x, y)
