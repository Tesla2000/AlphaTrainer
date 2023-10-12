from splendor.data.Game import Game
from splendor.data.Tier import Tier
from splendor.processing.moves.Move import Move


class Build(Move):
    def __init__(self, tier: Tier, index: int):
        self.tier = tier
        self.index = index

    def perform(self, game: Game) -> None:
        current_player = game.current_player
        card = self.tier.pop(self.index)
        current_player.resources -= card.cost
        current_player.cards.append(card)

    def is_valid(self, game: Game) -> bool:
        card = self.tier.pop(self.index)
        current_player = game.current_player
        return (
            not (
                current_player.resources + current_player.production - card.cost
            ).lacks()
            and len(self.tier.visible) >= self.index
        )
