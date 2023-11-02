from abc import abstractmethod, ABC
from typing import Sequence, Any, TYPE_CHECKING, Self

from alpha_trainer.classes.AlphaGameResult import AlphaGameResult

from alpha_trainer.classes.AlphaPlayer import AlphaPlayer

if TYPE_CHECKING:
    from alpha_trainer.classes.AlphaMove import AlphaMove


AlphaGameResults = dict[int, AlphaGameResult]


class AlphaTrainableGame(ABC):
    current_player: Any
    players: list
    current_player: AlphaPlayer
    players: Sequence[AlphaPlayer]

    @abstractmethod
    def copy(self) -> Self:
        pass

    @abstractmethod
    def perform(self, action: "AlphaMove") -> Self:
        pass

    @abstractmethod
    def get_possible_actions(self) -> list["AlphaMove"]:
        pass

    @abstractmethod
    def is_terminal(self) -> bool:
        pass

    @abstractmethod
    def get_results(self) -> AlphaGameResults:
        pass

    @abstractmethod
    def get_state(self) -> tuple:
        pass
