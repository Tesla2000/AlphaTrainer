from pathlib import Path

import numpy as np

from GameLogic.create_training_data import save_game_results
from train_model import train_to_predict_move


def main():
    max_n_sample = 1_000_000
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    n_files = len(tuple(results_dir.iterdir()))
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
        save_game_results(1, 10_000, file_name, current_model, 1 + i / 10)
        data = np.append(
            data,
            np.loadtxt(f"results/results_{i}.csv", delimiter=",", dtype=int),
            axis=0,
        )[:max_n_sample]
        current_model = train_to_predict_move(data)


if __name__ == "__main__":
    main()
