from dataclasses import dataclass, field

from splendor.data.Card import Card


@dataclass
class PlayerReserve:
    cards: tuple[Card] = field(default_factory=tuple)

    def can_add(self) -> bool:
        return len(self.cards) < 3

    def append(self, card: Card) -> None:
        if not self.can_add():
            raise ValueError(f"Can't add card to reserve {self.cards}")
        cards = list(self.cards)
        cards.append(card)
        self.cards = tuple(cards)

    def pop(self, index: int) -> Card:
        cards = list(self.cards)
        card = cards.pop(index)
        self.cards = tuple(cards)
        return card

    def __getitem__(self, item) -> Card:
        return self.cards.__getitem__(item)

    def __len__(self) -> int:
        return len(self.cards)
