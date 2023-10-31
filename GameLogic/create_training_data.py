from pathlib import Path

from sklearn.tree import DecisionTreeClassifier

from GameLogic.simulate_games import simulate_game


def save_game_results(
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
        nodes = simulate_game(n_simulations, model, model_decision_weight)
        for node in nodes:
            print(
                f"{node.value / node.visits},{','.join(map(str, map(int, node.state.get_state())))}",
                file=output,
            )
    output.close()
