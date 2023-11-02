import math
import random
from typing import Optional, Self

from tqdm import tqdm

from alpha_trainer.classes.AlphaMove import AlphaMove
from alpha_trainer.classes.AlphaTrainableGame import (
    AlphaTrainableGame,
    AlphaGameResults,
)


class Node:
    def __init__(self, state: AlphaTrainableGame, parent: Optional[Self] = None):
        self.state = state
        self.parent = parent
        self.children = {}
        self.visits = 0
        self.value = 0

    def is_fully_expanded(self):
        return len(self.children) == len(list(self.state.get_possible_actions()))


def mcts_search(
    root_state: AlphaTrainableGame, num_simulations: int
) -> AlphaTrainableGame:
    root_node = Node(root_state)

    for _ in tqdm(range(num_simulations), desc="Processing", unit="iteration"):
        node = root_node

        # Selection
        while not node.state.is_terminal() and node.is_fully_expanded():
            node = select_child(node)

        # Expansion
        if not node.state.is_terminal() and not node.is_fully_expanded():
            node = expand(node)

        # Simulation
        result = simulate(node.state.copy())

        # Backpropagation
        backpropagate(node, result)

    best_child = select_best_child(root_node)
    return best_child.state


def select_child(node: Node) -> Node:
    possible_actions = list(node.state.get_possible_actions())
    if not node.is_fully_expanded():
        return expand(node)
    else:
        best_child = None
        best_uct = -float("inf")
        for action in possible_actions:
            child = node.children[action]
            uct = (child.value / (child.visits + 1)) + (
                math.sqrt(2 * math.log(node.visits) / (child.visits + 1))
            )
            if uct > best_uct:
                best_uct = uct
                best_child = child
        return best_child


def expand(node: Node) -> Node:
    possible_actions = list(node.state.get_possible_actions())
    untried_actions = [
        action for action in possible_actions if action not in node.children
    ]
    action: AlphaMove = random.choice(untried_actions)
    new_state = node.state.copy()
    new_state.perform(action)
    new_node = Node(new_state, parent=node)
    node.children[action] = new_node
    return new_node


def simulate(state: AlphaTrainableGame) -> AlphaGameResults:
    while not state.is_terminal():
        possible_actions = state.get_possible_actions()
        action: AlphaMove = random.choice(possible_actions)
        state.perform(action)
    return state.get_results()


def backpropagate(node: Node, results: AlphaGameResults) -> None:
    while node is not None:
        node.visits += 1
        node.value += results[node.state.current_player.id].value
        node = node.parent


def select_best_child(node: Node) -> Node:
    best_child = None
    best_value = -float("inf")
    for child in node.children.values():
        child_value = child.value / child.visits
        if child_value > best_value:
            best_value = child_value
            best_child = child
    return best_child
