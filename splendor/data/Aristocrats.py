from splendor.data.Aristocrat import Aristocrat, empty_aristocrat
from splendor.data.BasicResources import BasicResources
from dataclasses import dataclass


@dataclass(slots=True)
class Aristocrats:
    aristocrats: list[Aristocrat]

    def pop(self, index: int) -> "Aristocrat":
        aristocrat = self.aristocrats.pop(index)
        self.aristocrats.append(empty_aristocrat)
        return aristocrat
