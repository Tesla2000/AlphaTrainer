from itertools import islice
from pathlib import Path

from splendor.data.Card import Card
from splendor.data.Tier import Tier


def generate_tiers() -> list[Tier]:
    building_data = iter(Path("buildings.csv").read_text().splitlines())
    next(building_data)
    tiers = list(
        Tier(list(map(Card.from_text, islice(building_data, stop))))
        for stop in (40, 30, 20)
    )
    return tiers
