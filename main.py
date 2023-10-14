from collections import defaultdict
from pathlib import Path
from typing import Iterable

import numpy as np

from alpha_trainer.classes.AlphaMove import AlphaMove
from alpha_trainer.classes.AlphaTrainableGame import AlphaTrainableGame
from alpha_trainer.exceptions.GameFinishedException import GameFinishedException
from alpha_trainer.exceptions.NoPossibleMoveException import NoPossibleMoveException
from splendor.processing.Game import Game


def get_preference(_: Iterable[float]) -> Iterable[int]:
    return np.argsort(np.random.random(45))


def choose_move(
    game: AlphaTrainableGame, state: Iterable, all_moves: list[AlphaMove]
) -> tuple[AlphaMove, int]:
    for move_index in get_preference(state):
        if all_moves[move_index].is_valid(game):
            return all_moves[move_index], move_index
    raise NoPossibleMoveException()


def play_a_game(x: list, y: list):
    game = Game()
    states = defaultdict(list)
    while True:
        current_player = game.current_player
        state = game.get_state()
        try:
            move, move_index = choose_move(game, state, game.all_moves)
        except NoPossibleMoveException:
            break
        states[id(current_player)].append(state + [move_index])
        move.perform(game)
        try:
            game.next_turn()
        except GameFinishedException as e:
            winner_id = id(e.args[0])
            for player in game.players:
                player_id = id(player)
                x += states[player_id]
                if player_id == winner_id:
                    y += len(states[player_id]) * [1]
                else:
                    y += len(states[player_id]) * [0]
            break


def save_results(n_games: int):
    results_folder = Path("results")
    results_folder.mkdir(exist_ok=True)
    results_file = results_folder / "splendor"
    output = results_file.open("w")
    for _ in range(n_games):
        x, y = [], []
        play_a_game(x, y)
        for state, result in zip(x, y):
            print(f"{result};{','.join(map(str, state))}", file=output)
    output.close()


def main():
    save_results(1000)


if __name__ == "__main__":
    main()
