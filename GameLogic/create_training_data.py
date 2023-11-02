from pathlib import Path
from typing import Type

from sklearn.tree import DecisionTreeClassifier

from GameLogic.simulate_games import simulate_game
from alpha_trainer.classes.AlphaTrainableGame import AlphaTrainableGame


def save_game_results(
    game_class: Type[AlphaTrainableGame],
    n_games: int,
    n_simulations: int,
    file_name: str,
    model: DecisionTreeClassifier = None,
    model_decision_weight: float = 1,
) -> None:
    results_folder = Path("results")
    results_folder.mkdir(exist_ok=True)
    results_file = results_folder / file_name
    output = results_file.open("w")
    for _ in range(n_games):
        results = simulate_game(game_class, n_simulations, model, model_decision_weight)
        for state, result in results.items():
            print(
                f"{result},{','.join(map(str, map(int, state)))}",
                file=output,
            )
    output.close()
