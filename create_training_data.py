import random
from pathlib import Path
from typing import Type

from alpha_trainer import AlphaMove
from alpha_trainer.expansion_login.simulate_games import simulate_game
from alpha_trainer.classes.AlphaTrainableGame import AlphaTrainableGame


def save_game_results(
    game_class: Type[AlphaTrainableGame],
    file_name: str,
    n_simulations: int = None,
    model=None,
) -> None:
    results_folder = Path("results")
    results_folder.mkdir(exist_ok=True)
    results_file = results_folder / file_name
    output = results_file.open("w")
    results = simulate_game(
        game_class, n_simulations, model, choice_function=choice_function
    )
    for state, result in results.items():
        print(
            f"{result},{','.join(map(str, map(int, state)))}",
            file=output,
        )
    output.close()


def choice_function(probabilities: dict[AlphaMove, float]) -> AlphaMove:
    filtered_probabilities = dict(
        sorted(probabilities.items(), key=lambda probability: -probability[1])[:2]
    )
    return random.choices(
        tuple(filtered_probabilities.keys()), filtered_probabilities.values(), k=1
    )[0]
