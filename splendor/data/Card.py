from typing import NamedTuple

from splendor.data.Resource import Resource
from splendor.data.Resources import Resources


class Card(NamedTuple):
    production: Resource
    cost: Resources
    points: int = 0

    @classmethod
    def from_text(cls, line: str) -> "Card":
        tier, production, points, name, white, blue, green, red, black = line.split(",")
        cost = Resources(*tuple(map(int, (red, green, blue, black, white))))
        production = Resource(production)
        return Card(production, cost, int(points))


empty_card = Card(Resource.GOLD, Resources(), -1)
