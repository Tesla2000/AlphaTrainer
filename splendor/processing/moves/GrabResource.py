from splendor.processing._Game import _Game
from splendor.data.Resources import Resources
from splendor.processing.moves.Move import Move


class GrabResource(Move):
    def __init__(self, resources: Resources):
        self.resources = resources

    def perform(self, game: _Game) -> None:
        game.board.resources -= self.resources
        game.current_player.resources += self.resources

    def is_valid(self, game: _Game) -> bool:
        return not (game.board.resources - self.resources).lacks()

    def __repr__(self):
        return self.resources.__repr__()
