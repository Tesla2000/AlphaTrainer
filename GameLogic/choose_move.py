from nltk import DecisionTreeClassifier

from alpha_trainer.classes.AlphaMove import AlphaMove
from alpha_trainer.classes.AlphaTrainableGame import AlphaTrainableGame
from alpha_trainer.exceptions.NoPossibleMoveException import NoPossibleMoveException
from main import get_preference


def choose_move(
    game: AlphaTrainableGame,
    state: list,
    all_moves: list[AlphaMove],
    model: DecisionTreeClassifier = None,
    model_decision_weight: float = 1,
) -> tuple[AlphaMove, int]:
    for move_index in get_preference(state, model, model_decision_weight):
        if all_moves[move_index].is_valid(game):
            return all_moves[move_index], move_index
    raise NoPossibleMoveException()
