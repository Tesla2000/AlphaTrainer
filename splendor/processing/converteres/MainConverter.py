from typing import Any


class Converter:
    @classmethod
    def convert(cls, element: Any) -> list:
        for converter in cls.__subclasses__():
            element = converter.convert(element)
        return list(element)
