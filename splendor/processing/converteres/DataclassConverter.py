from dataclasses import astuple
from typing import Any

from splendor.processing.converteres.MainConverter import Converter


class DataclassConverter(Converter):
    @classmethod
    def convert(cls, potential_dataclass: Any) -> Any:
        if not hasattr(potential_dataclass, "__dataclass_fields__"):
            return potential_dataclass
        return astuple(potential_dataclass)
