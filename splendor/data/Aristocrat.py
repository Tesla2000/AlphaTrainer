from typing import NamedTuple


class Aristocrat(NamedTuple):
    points: int
    cost_red: int = 0
    cost_green: int = 0
    cost_blue: int = 0
    cost_brown: int = 0
    cost_white: int = 0
