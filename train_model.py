import numpy as np
from sklearn.model_selection import train_test_split


def train_to_predict_move(model, data: list[np.array]):
    try:
        train, test = train_test_split(tuple(filter(len, data)), test_size=0.2)
    except ValueError:
        return model, 0.5
    y_train, x_train = np.concatenate(train)[:, 0], np.concatenate(train)[:, 1:]
    y_test, x_test = np.concatenate(test)[:, 0], np.concatenate(test)[:, 1:]
    model.fit(x_train, y_train)
    return model, model.score(x_test, y_test)
