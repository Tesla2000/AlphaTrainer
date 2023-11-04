import random

from alpha_trainer.classes.AlphaMove import AlphaMove
from alpha_trainer.expansion_login.mcts_search.Node import Node


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
