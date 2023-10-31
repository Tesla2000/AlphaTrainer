from abc import abstractmethod, ABC
from typing import Generator, Sequence, Any, TYPE_CHECKING, Self

from alpha_trainer.classes.AlphaGameResult import AlphaGameResult

from alpha_trainer.classes.AlphaPlayer import AlphaPlayer

if TYPE_CHECKING:
    from alpha_trainer.classes.AlphaMove import AlphaMove


class AlphaTrainableGame(ABC):
    current_player: Any
    players: list
    current_player: AlphaPlayer
    players: Sequence[AlphaPlayer]

    @abstractmethod
    def copy(self) -> Self:
        pass

    @abstractmethod
    def get_possible_actions(self) -> Generator["AlphaMove", None, None]:
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
