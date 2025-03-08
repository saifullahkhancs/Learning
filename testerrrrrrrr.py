from pydantic import BaseModel, root_validator
from typing import Optional, Union, List


def unique_list(input_list):
    unique_elements = []
    seen = set()

    for element in input_list:
        # For dictionaries, use tuple of items for uniqueness
        if isinstance(element, dict):
            element_key = tuple(sorted(element.items()))
            # For lists, use tuple of items for uniqueness
        elif isinstance(element, list):
            element_key = tuple(map(repr, element))  # Use repr to handle unhashable items
        else:
            element_key = repr(element)  # Use repr for other types to create a hashable version

        if element_key not in seen and element not in ["", None]:
            seen.add(element_key)
            unique_elements.append(element)

    return unique_elements

class Intel(BaseModel):
    name: Optional[Union[str, list]]
    strike: Optional[list]
    strikes_count: Optional[int]
    strike_id: Optional[list]
    def __init__(self, **data):
        # for v, k in data.items():
        #     if isinstance(k, list) and len(k) > 0:
        #         data[v] = unique_list(k)
        if data.get('strike'):
            data['strike'] = list(set(data.get('strike')))
            if not data.get('strike_id'):
                data['strike_id'] = list(
                    set([name.split('-')[0].strip().upper() if '-' in name else name for name in data['strike']]))
            else:
                st_ids = list(
                    set([name.split('-')[0].strip().upper() if '-' in name else name for name in data['strike']]))
                data['strike_id'].extend(st_ids)
        if data.get('strike_id'):
            data['strike_id'] = list(set(data.get('strike_id')))
            data['strikes_count'] = len(data['strike_id'])

        super().__init__(**data)

    @root_validator(pre=True)
    def validate_list_properties(cls, values):
        for key, value in values.items():
            if isinstance(value, list):
                values[key] = [i for i in value if i not in [None, ""]]
        return values



data = {
    "strike_id": [""],
    "strike":[""],
    "strikes_count": 0,
    "name":"ali"
}
mapped_data = Intel(**data)
print(mapped_data)