from dataclasses import dataclass, field
import random

from splendor.data.AllResources import AllResources
from splendor.data.Aristocrat import Aristocrat
from splendor.data.Tier import Tier
from splendor.data.game_setup.generate_aristocrats import generate_aristocrats
from splendor.data.game_setup.generate_tiers import generate_tiers


@dataclass(slots=True)
class Board:
    n_players: int = 2
    tiers: list[Tier] = field(init=False, default_factory=generate_tiers)
    aristocrats: list[Aristocrat] = field(
        init=False, default_factory=generate_aristocrats
    )
    resources: AllResources = field(init=False)

    def __post_init__(self):
        self.resources = AllResources(*5 * [{2: 4, 3: 5, 4: 7}[self.n_players]])
        self.resources.gold = 5
        random.shuffle(self.aristocrats)
        self.aristocrats = self.aristocrats[: self.n_players + 1]
