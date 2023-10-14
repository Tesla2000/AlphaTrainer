from abc import abstractmethod
from typing import Iterable

from alpha_trainer.classes.AlphaMove import AlphaMove, _AlphaTrainableGame


class AlphaTrainableGame(_AlphaTrainableGame):
    @abstractmethod
    def get_state(self) -> Iterable:
        pass

    @abstractmethod
    def copy(self) -> "AlphaTrainableGame":
        pass

    @property
    @abstractmethod
    def all_moves(self) -> list[AlphaMove]:
        pass

    @abstractmethod
    def next_turn(self) -> None:
        pass
