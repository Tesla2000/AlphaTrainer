from itertools import count
from pathlib import Path
from statistics import mean

import numpy as np
from IPython import display
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from tqdm import tqdm

from PySplendor.Game import Game
from create_training_data import save_game_results
from train_model import train_to_predict_move


def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title("Training...")
    plt.xlabel("Number of Games")
    plt.ylabel("Score")
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=min(scores))
    plt.text(len(scores) - 1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(0.1)


def main():
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    files = tuple(results_dir.iterdir())
    model = DecisionTreeClassifier()
    scores, mean_scores, data = [], [], []
    max_number = 0
    if files:
        data = list(
            np.loadtxt(file, delimiter=",", dtype=int)
            for file in files
            if file.stat().st_size
        )
        model, score = train_to_predict_move(model, data)
        scores.append(score)
        max_number = int(
            "".join(
                filter(
                    str.isnumeric,
                    max(files, key=lambda file: (len(file.name), file.name)).name,
                )
            )
        )
    game_class = Game
    plt.ion()

    for i in tqdm(count(max_number + 1)):
        file_name = f"results_{i}.csv"
        save_game_results(game_class, file_name, model=None, n_simulations=100)
        data.append(np.loadtxt(f"results/results_{i}.csv", delimiter=",", dtype=int))
        model, score = train_to_predict_move(model, data)
        scores.append(score)
        mean_scores.append(mean(scores))
        plot(scores, mean_scores)


if __name__ == "__main__":
    main()
