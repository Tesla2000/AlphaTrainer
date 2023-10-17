from splendor.data.BasicResources import BasicResources
from dataclasses import dataclass


@dataclass(slots=True)
class Aristocrat:
    points: int
    cost: BasicResources

    @classmethod
    def from_text(cls, line: str) -> "Aristocrat":
        points, white, blue, green, red, black = map(int, line.split(","))
        cost = BasicResources(red, green, blue, black, white)
        return Aristocrat(points, cost)


empty_aristocrat = Aristocrat(0, BasicResources())
