from sklearn.tree import DecisionTreeClassifier

from GameLogic.MCTS import Node, simulate, backpropagate
from PySplendor.Game import Game


def simulate_games(
    iterations: int,
    n_move_to_consider_state: int,
    model: DecisionTreeClassifier = None,
    model_decision_weight: float = 1,
):
    game = Game()
    root = Node(game)
    for _ in range(iterations):
        node = simulate(root)
        backpropagate(node)
    pass
