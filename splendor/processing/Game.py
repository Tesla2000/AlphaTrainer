import operator
from dataclasses import astuple
from functools import reduce
from itertools import combinations, starmap, product

from alpha_trainer.exceptions.GameFinishedException import GameFinishedException
from alpha_trainer.classes.AlphaMove import AlphaMove
from splendor.data.Resource import Resource
from splendor.data.Resources import Resources
from splendor.processing._Game import _Game
from splendor.processing.converteres import Converter
from splendor.processing.moves.BuildBoard import BuildBoard
from splendor.processing.moves.BuildReserve import BuildReserve
from splendor.processing.moves.GrabResource import GrabResource
from splendor.processing.moves.ReserveTop import ReserveTop
from splendor.processing.moves.ReserveVisible import ReserveVisible


class Game(_Game):
    def __init__(self, n_players: int = 2):
        super().__init__(n_players)
        self._all_moves = None
        self._performed_the_last_move = dict(
            (id(player), False) for player in self.players
        )
        self._last_turn = False

    def next_turn(self) -> None:
        self.players = next(self.player_order)
        if self.current_player.points >= 15 or self._last_turn:
            self._last_turn = True
        self._performed_the_last_move[id(self.current_player)] = self._last_turn
        if all(self._performed_the_last_move.values()):
            raise GameFinishedException([])
        self.current_player = self.players[0]

    def get_state(self) -> list:
        state = []
        points, tiers, aristocrats, resources = astuple(self.board)
        state += [points, *resources]
        state += reduce(
            operator.add,
            (
                list(Converter.convert(field))
                for tier in tiers
                for card in tier[1]
                for field in card
            ),
        )
        for player in self.players:
            state += astuple(player.resources, tuple_factory=list)
            state += astuple(player.production, tuple_factory=list)
            state.append(len(player.reserve))
            state.append(player.points)
        return state

    def copy(self) -> "AlphaTrainableGame":
        pass

    @property
    def all_moves(self) -> list[AlphaMove]:
        if self._all_moves:
            return self._all_moves
        valid_resources = tuple(resource for resource in Resource.__members__.values())
        combos = combinations([{resource.value: 1} for resource in valid_resources], 3)
        all_moves = list(
            GrabResource(Resources(**res_1, **res_2, **res_3))
            for res_1, res_2, res_3 in combos
        )
        all_moves += list(
            GrabResource(Resources(**{resource.value: 2}))
            for resource in valid_resources
        )
        all_moves += list(starmap(BuildBoard, product(range(3), range(4))))
        all_moves += list(map(BuildReserve, range(3)))
        all_moves += list(starmap(ReserveVisible, product(range(3), range(4))))
        all_moves += list(map(ReserveTop, range(3)))
        self._all_moves = all_moves
        return all_moves
