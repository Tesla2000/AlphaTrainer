from abc import abstractmethod
from typing import Generator, Sequence

from alpha_trainer.classes.AlphaGameResult import AlphaGameResult
from alpha_trainer.classes.AlphaMove import AlphaMove
from alpha_trainer.classes.AlphaPlayer import AlphaPlayer
from alpha_trainer.classes.AlphaTrainableGamePrototype import (
    AlphaTrainableGamePrototype,
)


class AlphaTrainableGame(AlphaTrainableGamePrototype):
    current_player: AlphaPlayer
    players: Sequence[AlphaPlayer]

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
