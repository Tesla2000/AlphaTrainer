from collections import Counter
from dataclasses import asdict

from splendor.data.Resources import Resources
from splendor.processing._Game import _Game
from splendor.processing.moves.Move import Move


class BuildBoard(Move):
    def __init__(self, tier_index: int, index: int):
        self.tier_index = tier_index
        self.index = index

    def perform(self, game: _Game) -> None:
        current_player = game.current_player
        tier = game.board.tiers[self.tier_index]
        card = tier.pop(self.index)
        not_produced = Resources(
            **(Counter(asdict(card.cost)) - Counter(asdict(current_player.production)))
        )
        current_player.resources -= not_produced
        current_player.cards.append(card)

    def is_valid(self, game: _Game) -> bool:
        tier = game.board.tiers[self.tier_index]
        if len(tier.visible) <= self.index:
            return False
        card = tier.visible[self.index]
        current_player = game.current_player
        return not (
            current_player.resources + current_player.production - card.cost
        ).lacks()
