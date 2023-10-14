from typing import Any

from splendor.processing.converteres.MainConverter import Converter


class NumberConverter(Converter):
    @classmethod
    def convert(cls, potential_resource: Any) -> Any:
        if not isinstance(potential_resource, int | float):
            return potential_resource
        return [potential_resource]
