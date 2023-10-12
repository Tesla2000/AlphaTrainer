from splendor.data.Game import Game
from splendor.data.Resources import Resources
from splendor.processing.moves.Move import Move


class GrabResource(Move):
    def __init__(self, resources: Resources):
        self.resources = resources

    def perform(self, game: Game) -> None:
        game.board.resources -= self.resources
        game.current_player.resources += self.resources

    def is_valid(self, game: Game) -> bool:
        return not (game.board.resources - self.resources).lacks()
