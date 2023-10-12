from splendor.data.Game import Game
from splendor.processing.moves.Reserve import Reserve


class ReserveTop(Reserve):
    def perform(self, game: Game) -> None:
        card = self.tier.hidden.pop()
        self.reserve_card(game, card)

    def is_valid(self, game: Game) -> bool:
        return bool(self.tier.hidden) and len(game.current_player.reserve.cards) < 3
