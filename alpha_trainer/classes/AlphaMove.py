from abc import ABC, abstractmethod

from alpha_trainer.classes.AlphaTrainableGamePrototype import (
    AlphaTrainableGamePrototype,
)


class AlphaMove(ABC):
    @abstractmethod
    def perform(self, game: AlphaTrainableGamePrototype) -> AlphaTrainableGamePrototype:
        pass

    @abstractmethod
    def is_valid(self, game: AlphaTrainableGamePrototype) -> bool:
        pass
