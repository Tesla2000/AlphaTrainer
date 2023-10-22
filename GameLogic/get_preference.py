import numpy as np
from sklearn.tree import DecisionTreeClassifier

from PySplendor.Game import n_moves


def get_preference(
    state: list[int],
    model: DecisionTreeClassifier = None,
    model_decision_weight: float = 1,
) -> np.array:
    if model:
        probabilities = np.array(
            tuple(model.predict_proba(np.array(state).reshape(1, -1)))
        )[0]
    else:
        probabilities = np.zeros(n_moves)
    return np.argsort(np.random.random(n_moves) + probabilities * model_decision_weight)
