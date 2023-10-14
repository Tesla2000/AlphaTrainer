from dataclasses import dataclass
import random

from splendor.data.Aristocrat import Aristocrat
from splendor.data.Resource import Resource
from splendor.data.Resources import Resources
from splendor.data.Tier import Tier


@dataclass
class Board:
    n_players: int
    tiers: list[Tier] = None
    aristocrats: list[Aristocrat] = None
    resources: Resources = None

    def __post_init__(self):
        self.resources = Resources(
            **dict(
                (resource, {2: 4, 3: 5, 4: 7}[self.n_players])
                for resource in Resource.__members__.values()
            )
        )
        self.resources.gold = 5
        random.shuffle(self.aristocrats)
        self.aristocrats = self.aristocrats[: self.n_players + 1]
