from splendor.data.Game import Game
from splendor.processing.moves.Reserve import Reserve


class ReserveTop(Reserve):
    def perform(self, game: Game) -> None:
        tier = game.board.tiers[self.tier_index]
        card = tier.hidden.pop()
        self.reserve_card(game, card)

    def is_valid(self, game: Game) -> bool:
        tier = game.board.tiers[self.tier_index]
        return bool(tier.hidden) and len(game.current_player.reserve.cards) < 3
