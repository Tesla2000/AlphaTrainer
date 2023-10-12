from abc import ABC

from splendor.data.Card import Card
from splendor.data.Game import Game
from splendor.data.Tier import Tier
from splendor.processing.moves.Move import Move


class Reserve(Move, ABC):
    def __init__(self, tier: Tier):
        self.tier = tier

    def reserve_card(self, game: Game, card: Card):
        current_player = game.current_player
        current_player.reserve.append(card)
        if game.board.resources.gold:
            game.board.resources.gold -= 1
            current_player.resources.gold += 1
