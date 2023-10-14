from splendor.processing._Game import _Game
from splendor.processing.moves.Reserve import Reserve


class ReserveVisible(Reserve):
    def __init__(self, tier_index: int, index: int):
        super().__init__(tier_index)
        self.index = index

    def perform(self, game: _Game) -> None:
        tier = game.board.tiers[self.tier_index]
        card = tier.pop(self.index)
        self.reserve_card(game, card)

    def is_valid(self, game: _Game) -> bool:
        tier = game.board.tiers[self.tier_index]
        return (
            len(tier.visible) >= self.index
            and len(game.current_player.reserve.cards) < 3
        )
