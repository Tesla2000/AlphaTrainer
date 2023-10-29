from pathlib import Path

from sklearn.tree import DecisionTreeClassifier

from GameLogic.simulate_games import simulate_games


def save_game_results(
    n_games: int,
    n_simulations: int,
    n_move_to_consider_state: int,
    file_name: str,
    model: DecisionTreeClassifier = None,
    model_decision_weight: float = 1,
) -> None:
    results_folder = Path("results")
    results_folder.mkdir(exist_ok=True)
    results_file = results_folder / file_name
    output = results_file.open("w")
    game_lengths = []
    for _ in range(n_games):
        x, y = [], []
        simulate_games(
            n_simulations, n_move_to_consider_state, model, model_decision_weight
        )
        game_lengths.append(len(y))
        for state, result in zip(x, y):
            print(f"{result},{','.join(map(str, map(int, state)))}", file=output)
    output.close()
