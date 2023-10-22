from abc import ABC, abstractmethod
from typing import Any


class AlphaTrainableGamePrototype(ABC):
    current_player: Any
    players: list

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def get_possible_actions(self):
        pass

    @abstractmethod
    def next_turn(self):
        pass

    @abstractmethod
    def is_terminal(self):
        pass

    @abstractmethod
    def get_result(self, player):
        pass

    @abstractmethod
    def get_state(self):
        pass
