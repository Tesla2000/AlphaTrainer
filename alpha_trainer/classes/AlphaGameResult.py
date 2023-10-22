from dataclasses import dataclass


@dataclass(frozen=True)
class AlphaGameResult:
    value: int

    def __post_init__(self):
        if self.value not in (-1, 0, 1):
            raise ValueError
