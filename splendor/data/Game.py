from _typeshed import SupportsNext
from dataclasses import dataclass, field
from itertools import cycle

from splendor.data.Board import Board
from splendor.data.player.Player import Player


@dataclass
class Game:
    n_players: int = 2
    players: list[Player] = field(init=False)
    board: Board = field(init=False)
    player_order: SupportsNext[Player] = field(init=False)
    current_player: Player = field(init=False)

    def __post_init__(self):
        self.players = list(Player() for _ in range(self.n_players))
        self.board = Board(self.n_players)
        self.player_order = cycle(self.players)
        self.current_player = next(self.player_order)
