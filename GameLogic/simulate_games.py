from sklearn.tree import DecisionTreeClassifier
from tqdm import tqdm

from GameLogic.MCTS import Node, simulate, backpropagate
from PySplendor.Game import Game


def simulate_game(
    iterations: int,
    model: DecisionTreeClassifier = None,
    model_decision_weight: float = 1,
):
    game = Game.create()
    root = Node(game)
    for _ in tqdm(range(iterations), desc="Processing", unit="iteration"):
        node = simulate(root)
        backpropagate(node)
    return
