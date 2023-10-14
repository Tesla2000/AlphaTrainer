from abc import ABC, abstractmethod


class _AlphaTrainableGame(ABC):
    pass


class AlphaMove(ABC):
    @abstractmethod
    def perform(self, game: _AlphaTrainableGame) -> None:
        pass

    @abstractmethod
    def is_valid(self, game: _AlphaTrainableGame) -> bool:
        pass
