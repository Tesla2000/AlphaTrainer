import random
from dataclasses import dataclass, field
from itertools import compress
from math import sqrt, log, exp
from typing import Optional

from alpha_trainer.classes.AlphaMove import AlphaMove
from alpha_trainer.classes.AlphaTrainableGame import (
    AlphaTrainableGame,
)


@dataclass
class Node:
    state: AlphaTrainableGame
    parent: "Node" = field(default=None)
    children: list[Optional["Node"]] = field(init=False, default_factory=list)
    visits: int = field(init=False, default=0)
    value: int = field(init=False, default=0)
    terminal: bool = field(init=False, default=False)
    all_actions: tuple[AlphaMove] = field(init=False, default=None)


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


def score_position(node: Optional[Node]) -> float:
    if node is None:
        return 1.0
    return exp(node.value / node.visits)


def simulate(node: Node) -> Node:
    while not node.state.is_terminal():
        new_node = Node(node.state.copy(), node)
        if not node.children:
            if not (actions := tuple(node.state.get_possible_actions())):
                node.terminal = True
                return node
            node.all_actions = actions
            node.children = len(actions) * [None]
        extendable = tuple(map(lambda n: n is None or not n.terminal, node.children))
        actions = tuple(compress(node.all_actions, extendable))
        if not actions:
            node.terminal = True
            return node
        action = random.choices(
            actions, weights=tuple(map(score_position, node.children)), k=1
        )[0]
        index = actions.index(action)
        if node.children[index]:
            return node.children[index]
        new_node.state = action.perform(new_node.state)
        new_node.state.next_turn()
        node.children[index] = new_node
        node = new_node
    node.terminal = True
    return node


def backpropagate(node: Node):
    end_results = dict(
        (player.id, node.state.get_result(player)) for player in node.state.players
    )
    while True:
        node.visits += 1
        node.value += end_results[node.state.current_player.id].value
        node = node.parent
        if not node:
            break
        if all(n and n.terminal for n in node.children):
            node.terminal = True
