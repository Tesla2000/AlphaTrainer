from abc import abstractmethod
from typing import Generator

from GameLogic.MCTS import Node, select, expand, simulate, backpropagate
from alpha_trainer.classes.AlphaGameResult import AlphaGameResult
from alpha_trainer.classes.AlphaMove import AlphaMove
from alpha_trainer.classes.AlphaPlayer import AlphaPlayer
from alpha_trainer.classes.AlphaTrainableGamePrototype import (
    AlphaTrainableGamePrototype,
)


class AlphaTrainableGame(AlphaTrainableGamePrototype):
    current_player: AlphaPlayer
    players: list[AlphaPlayer]

    @abstractmethod
    def copy(self) -> "AlphaTrainableGame":
        pass

    @abstractmethod
    def get_possible_actions(self) -> Generator[AlphaMove, None, None]:
        pass

    @abstractmethod
    def next_turn(self) -> None:
        pass

    @abstractmethod
    def is_terminal(self) -> bool:
        pass

    @abstractmethod
    def get_result(self, player: AlphaPlayer) -> AlphaGameResult:
        pass

    @abstractmethod
    def get_state(self):
        pass

    def get_best_state(self, iterations: int) -> "AlphaTrainableGamePrototype":
        root = Node(self)
        current_player = self.current_player
        for _ in range(iterations):
            node = select(root)
            if not node.state.is_terminal():
                node = expand(node)
                result = simulate(node, current_player)
            else:
                result = node.state.get_result(current_player)
            backpropagate(node, result)
        return max(root.children, key=lambda n: n.visits).state
