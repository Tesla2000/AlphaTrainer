from dataclasses import dataclass, asdict, astuple


@dataclass(slots=True)
class Resources:
    red: int = 0
    green: int = 0
    blue: int = 0
    black: int = 0
    white: int = 0
    gold: int = 0

    def __sub__(self, other: "Resources") -> "Resources":
        if not isinstance(other, Resources):
            raise ValueError(f"Other element must be resource is {other.__class__}")
        self_dict = asdict(self)
        other_dict = asdict(other)
        return Resources(
            **dict((key, value - other_dict[key]) for key, value in self_dict.items())
        )

    def __add__(self, other: "Resources") -> "Resources":
        if not isinstance(other, Resources):
            raise ValueError(f"Other element must be resource is {other.__class__}")
        self_dict = asdict(self)
        other_dict = asdict(other)
        return Resources(
            **dict((key, value + other_dict[key]) for key, value in self_dict.items())
        )

    def lacks(self) -> bool:
        return any(resource < 0 for resource in astuple(self))
