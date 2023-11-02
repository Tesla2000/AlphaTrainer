from typing import Type

import numpy as np

from GameLogic.MCTS import mcts_search
from alpha_trainer.classes.AlphaTrainableGame import AlphaTrainableGame

StatesAndResults = dict[int, np.array]


def simulate_game(
    game_class: Type[AlphaTrainableGame],
    num_simulations: int = None,
    model=None,
    game_args: tuple = None,
    game_kwargs: dict = None,
) -> StatesAndResults:
    states = {}
    root = game_class(*(game_args or ()), **(game_kwargs or {}))
    states[root.get_state()] = root.current_player.id
    while not root.is_terminal():
        root = mcts_search(root, num_simulations)
        states[root.get_state()] = root.current_player.id
    return score_positions(root, states)


def score_positions(
    game: AlphaTrainableGame, states: dict[np.array, int]
) -> StatesAndResults:
    results = game.get_results()
    return dict(
        (state, results[player_id].value) for state, player_id in states.items()
    )
