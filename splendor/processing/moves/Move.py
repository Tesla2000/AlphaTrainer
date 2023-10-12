from abc import ABC, abstractmethod

from splendor.data.Game import Game


class Move(ABC):
    @abstractmethod
    def perform(self, game: Game) -> None:
        pass

    @abstractmethod
    def is_valid(self, game: Game) -> bool:
        pass
