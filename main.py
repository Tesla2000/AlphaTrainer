from collections import defaultdict
from typing import Iterable

import numpy as np

from alpha_trainer.exceptions.GameFinishedException import GameFinishedException
from alpha_trainer.classes.AlphaMove import AlphaMove
from alpha_trainer.classes.AlphaTrainableGame import AlphaTrainableGame
from alpha_trainer.exceptions.NoPossibleMoveException import NoPossibleMoveException
from splendor.processing.Game import Game


def get_preference(_: Iterable[float]) -> Iterable[int]:
    return np.argsort(np.random.random(45))


def choose_move(
    game: AlphaTrainableGame, state: Iterable, all_moves: list[AlphaMove]
) -> AlphaMove:
    for move_index in get_preference(state):
        if all_moves[move_index].is_valid(game):
            return all_moves[move_index]
    raise NoPossibleMoveException()


def play_a_game():
    game = Game()
    states = defaultdict(list)
    while True:
        current_player = game.current_player
        state = game.get_state()
        try:
            move = choose_move(game, state, game.all_moves)
        except NoPossibleMoveException:
            break
        states[id(current_player)].append(state)
        move.perform(game)
        try:
            game.next_turn()
        except GameFinishedException:
            pass


def main():
    tuple(play_a_game() for _ in range(100))


if __name__ == "__main__":
    main()
