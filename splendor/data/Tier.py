import random
from dataclasses import field, dataclass

from splendor.data.Card import Card


@dataclass(slots=True)
class Tier:
    hidden: list[Card]
    visible: list[Card] = field(default_factory=list)

    def __post_init__(self):
        random.shuffle(self.hidden)
        for _ in range(4):
            self.visible.append(self.hidden.pop())

    def pop(self, index: int) -> Card:
        card = self.visible.pop(index)
        if self.hidden:
            self.visible.append(self.hidden.pop())
        return card
