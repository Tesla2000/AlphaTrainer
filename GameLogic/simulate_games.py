from sklearn.tree import DecisionTreeClassifier
from tqdm import tqdm

from GameLogic.MCTS import Node, simulate, backpropagate
from PySplendor.Game import Game


def simulate_games(
    iterations: int,
    n_move_to_consider_state: int,
    model: DecisionTreeClassifier = None,
    model_decision_weight: float = 1,
):
    game = Game.create()
    root = Node(game)
    for _ in tqdm(range(iterations), desc="Processing", unit="iteration"):
        node = simulate(root)
        backpropagate(node)
    return tuple(get_all_valid_nodes(root, n_move_to_consider_state))


def get_all_valid_nodes(node: Node, n_move_to_consider_state: int) -> Node:
    if not node:
        return
    if node.visits >= n_move_to_consider_state:
        yield node
        for child_node in node.children:
            for n in get_all_valid_nodes(child_node, n_move_to_consider_state):
                yield n
    return
