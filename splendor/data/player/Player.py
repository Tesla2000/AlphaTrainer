from dataclasses import dataclass, field

from splendor.data.Resources import Resources
from splendor.data.player.PlayerAristocrats import PlayerAristocrats
from splendor.data.player.PlayerCards import PlayerCards
from splendor.data.player.PlayerReserve import PlayerReserve


@dataclass
class Player:
    resources: Resources = field(default_factory=Resources)
    cards: PlayerCards = field(default_factory=PlayerCards)
    reserve: PlayerReserve = field(default_factory=PlayerReserve)
    aristocrats: PlayerAristocrats = field(default_factory=PlayerAristocrats)

    @property
    def points(self) -> int:
        return self.cards.points + self.aristocrats.points

    @property
    def production(self) -> Resources:
        return self.cards.production
