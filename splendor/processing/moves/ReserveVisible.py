from splendor.data.Game import Game
from splendor.data.Tier import Tier
from splendor.processing.moves.Reserve import Reserve


class ReserveVisible(Reserve):
    def __init__(self, tier: Tier, index: int):
        super().__init__(tier)
        self.index = index

    def perform(self, game: Game) -> None:
        card = self.tier.pop(self.index)
        self.reserve_card(game, card)

    def is_valid(self, game: Game) -> bool:
        return (
            len(self.tier.visible) >= self.index
            and len(game.current_player.reserve.cards) < 3
        )
