import random
from dataclasses import dataclass, field
from math import sqrt, log

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
    if node is None or node.visits == 0:
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


def simulate(node: Node) -> Node:
    while not node.state.is_terminal():
        new_node = Node(node.state.copy(), node)
        if not (actions := tuple(node.state.get_possible_actions())):
            return node
        if not node.children:
            node.children = len(actions) * [None]
        index = random.randint(0, len(actions) - 1)
        if node.children[index]:
            return node.children[index]
        action = actions[index]
        new_node.state = action.perform(new_node.state)
        new_node.state.next_turn()
        node.children[index] = new_node
        node = new_node
    return node


def backpropagate(node: Node):
    end_results = dict(
        (player.id, node.state.get_result(player)) for player in node.state.players
    )
    while node:
        node.visits += 1
        node.value += end_results[node.state.current_player.id].value
        node = node.parent
