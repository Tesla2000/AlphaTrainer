import random
from dataclasses import dataclass, field
from math import sqrt, log

from alpha_trainer.classes.AlphaGameResult import AlphaGameResult
from alpha_trainer.classes.AlphaPlayer import AlphaPlayer
from alpha_trainer.classes.AlphaTrainableGamePrototype import (
    AlphaTrainableGamePrototype,
)


@dataclass
class Node:
    state: AlphaTrainableGamePrototype
    parent: "Node" = field(default=None)
    children: list["Node"] = field(init=False, default_factory=list)
    visits: int = field(init=False, default=0)
    value: int = field(init=False, default=0)


def select(node: Node):
    while node.children:
        node = max(node.children, key=uct)
    return node


def uct(node: Node):
    if node.visits == 0:
        return float("inf")
    return (node.value / node.visits) + 1.0 * sqrt(
        log(node.parent.visits) / node.visits
    )


def expand(node: Node):
    actions = node.state.get_possible_actions()
    for action in actions:
        current_state_copy = node.state.copy()
        new_state = action.perform(current_state_copy)
        child = Node(new_state, parent=node)
        node.children.append(child)
    return random.choice(node.children)


def simulate(node: Node, player: AlphaPlayer):
    new_node = Node(node.state.copy())
    while not new_node.state.is_terminal():
        action = random.choice(tuple(new_node.state.get_possible_actions()))
        node.state = action.perform(new_node.state)
        new_node.state.next_turn()
    return new_node.state.get_result(player)


def backpropagate(node: Node, result: AlphaGameResult):
    while node:
        node.visits += 1
        node.value += result.value
        node = node.parent
