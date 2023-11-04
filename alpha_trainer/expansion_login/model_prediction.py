import random

from sklearn.exceptions import NotFittedError

from alpha_trainer.classes.AlphaTrainableGame import AlphaTrainableGame


def model_prediction(
    state: AlphaTrainableGame,
    model,
) -> AlphaTrainableGame:
    if not isinstance(state, AlphaTrainableGame):
        raise ValueError(
            f"State must be an instance of AlphaTrainableGame is {type(state)}"
        )
    probabilities = []
    possible_actions = state.get_possible_actions()
    for action in possible_actions:
        new_state = state.copy().perform(action)
        try:
            probability = model.predict_proba([new_state.get_state()])[0, 0] + 1e-12
        except NotFittedError:
            probability = random.random() + 1e-12
        probabilities.append(probability)
    chosen_action = random.choices(possible_actions, probabilities, k=1)[0]
    state = state.perform(chosen_action)
    return state
