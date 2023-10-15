from typing import Any

import numpy as np

from splendor.data.Resource import Resource
from splendor.processing.converteres.MainConverter import Converter

representations = np.eye(len(Resource.__members__) - 1)

res_to_list = dict(
    (resource, list(representations[index]))
    for index, resource in enumerate(Resource.__members__.keys())
    if resource != Resource.GOLD.name
)


class ResourceConverter(Converter):
    @classmethod
    def convert(cls, potential_resource: Any) -> Any:
        if not isinstance(potential_resource, Resource):
            return potential_resource
        return res_to_list.get(potential_resource.name, (0, 0, 0, 0, 0))
