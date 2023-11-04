from alpha_trainer.classes.AlphaTrainableGame import AlphaGameResults
from alpha_trainer.expansion_login.mcts_search.Node import Node


def backpropagate(node: Node, results: AlphaGameResults) -> None:
    while node is not None:
        node.visits += 1
        node.value += results[node.state.current_player.id].value
        node = node.parent
