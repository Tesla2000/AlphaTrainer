from abc import ABC, abstractmethod

from alpha_classes import (
    AlphaTrainableGame,
)


class AlphaMove(ABC):
    @abstractmethod
    def perform(self, game: AlphaTrainableGame) -> AlphaTrainableGame:
        pass

    @abstractmethod
    def is_valid(self, game: AlphaTrainableGame) -> bool:
        pass
