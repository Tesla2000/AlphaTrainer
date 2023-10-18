from collections import defaultdict
from pathlib import Path
from statistics import mean

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from tqdm import tqdm

from alpha_trainer.classes.AlphaMove import AlphaMove
from alpha_trainer.classes.AlphaTrainableGame import AlphaTrainableGame
from alpha_trainer.exceptions.GameFinishedException import GameFinishedException
from alpha_trainer.exceptions.NoPossibleMoveException import NoPossibleMoveException
from splendor import Game
from train_model import train_to_predict_move


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


def play_a_game(
    x: list,
    y: list,
    model: DecisionTreeClassifier = None,
    model_decision_weight: float = 1,
):
    game = Game()
    states = defaultdict(list)
    while True:
        current_player = game.current_player
        state = game.get_state()
        try:
            move, move_index = choose_move(
                game, state, game.all_moves, model, model_decision_weight
            )
        except NoPossibleMoveException:
            winner_id = id(game.players[-1])
            x += states[winner_id]
            y += len(states[winner_id]) * [1]
            break
        states[id(current_player)].append(state + [move_index])
        move.perform(game)
        try:
            game.next_turn()
        except GameFinishedException as e:
            winner_id = id(e.args[0])
            x += states[winner_id]
            y += len(states[winner_id]) * [1]
            break


def save_results(
    n_games: int,
    file_name: str,
    model: DecisionTreeClassifier = None,
    model_decision_weight: float = 1,
):
    results_folder = Path("results")
    results_folder.mkdir(exist_ok=True)
    results_file = results_folder / file_name
    output = results_file.open("w")
    game_lengths = []
    for _ in tqdm(range(n_games), desc="Processing", unit="iteration"):
        x, y = [], []
        play_a_game(x, y, model, model_decision_weight)
        game_lengths.append(len(y))
        for state, result in zip(x, y):
            print(f"{result},{','.join(map(str, map(int, state)))}", file=output)
    print(mean(game_lengths))
    output.close()


def main():
    max_n_sample = 1_000_000
    n_files = len(tuple(Path("results").iterdir()))
    current_model = None
    data = []
    # if n_files:
    #     data = np.concatenate(
    #         tuple(
    #             np.loadtxt(f"results/results_{i}.csv", delimiter=",", dtype=int)
    #             for i in range(n_files)
    #         )
    #     )
    #     current_model = train_to_predict_move(data)
    for i in range(n_files, n_files + 100):
        file_name = f"results_{i}.csv"
        save_results(1000, file_name, current_model, 1 + i / 10)
        data = np.append(
            data,
            np.loadtxt(f"results/results_{i}.csv", delimiter=",", dtype=int),
            axis=0,
        )[:max_n_sample]
        current_model = train_to_predict_move(data)


if __name__ == "__main__":
    main()
