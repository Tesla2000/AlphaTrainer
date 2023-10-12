from typing import NamedTuple

from splendor.data.Resource import Resource
from splendor.data.Resources import Resources


class Card(NamedTuple):
    production: Resource
    cost: Resources
    points: int = 0
