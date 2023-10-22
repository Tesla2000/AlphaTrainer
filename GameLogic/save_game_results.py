from pathlib import Path

from sklearn.tree import DecisionTreeClassifier
from tqdm import tqdm

from GameLogic.play_a_game import play_a_game


def save_game_results(
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
    output.close()
