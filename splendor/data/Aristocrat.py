from typing import NamedTuple

from splendor.data.Resources import Resources


class Aristocrat(NamedTuple):
    points: int
    cost: Resources

    @classmethod
    def from_text(cls, line: str) -> "Aristocrat":
        points, white, blue, green, red, black = map(int, line.split(","))
        cost = Resources(red, green, blue, black, white)
        return Aristocrat(points, cost)


empty_aristocrat = Aristocrat(0, Resources())
