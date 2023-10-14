from dataclasses import dataclass, field
import random

from splendor.data.Aristocrat import Aristocrat
from splendor.data.Resource import Resource
from splendor.data.Resources import Resources
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
    resources: Resources = field(init=False)

    def __post_init__(self):
        self.resources = Resources(
            **dict(
                (resource.value, {2: 400, 3: 500, 4: 700}[self.n_players])
                for resource in Resource.__members__.values()
            )
        )
        self.resources.gold = 5
        random.shuffle(self.aristocrats)
        self.aristocrats = self.aristocrats[: self.n_players + 1]
