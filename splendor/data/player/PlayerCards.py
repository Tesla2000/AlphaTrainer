from collections import Counter
from dataclasses import dataclass, field

from splendor.data.Card import Card
from splendor.data.Resources import Resources


@dataclass
class PlayerCards:
    cards: list[Card] = field(default_factory=list)

    @property
    def production(self) -> Resources:
        return Resources(**Counter(card.production for card in self.cards))

    @property
    def points(self) -> int:
        return sum(card.points for card in self.cards)

    def append(self, card: Card) -> None:
        self.cards.append(card)
