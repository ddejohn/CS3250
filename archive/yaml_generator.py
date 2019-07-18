import os
import yaml
import yaml_data
from random import sample
from random import choice
from random import randint


# def _write(make_type, make_num):
#     make_this = {
#         # "player": PlayerFactory,
#         "item": ItemFactory,
#     }[make_type]

#     fac = ItemFactory()

#     file_name = "./generic_" + make_type + "s.yml"
#     with open(file_name, "w") as save_file:
#         yaml.safe_dump(
#             {i: fac() for i in range(make_num)},
#             save_file, indent=4, width=80,
#             default_flow_style=False
#         )


class ItemFactory:
    qualities = yaml_data.QUALITIES
    descriptors = yaml_data.DESCRIPTORS
    materials = yaml_data.MATERIALS
    item_types = yaml_data.TYPES

    def __init__(self):
        this_item = list(self.item_types.keys())
        factories = {
            "weapon": self._make_uncommon,
            "armor": self._make_uncommon,
            "magic": self._make_uncommon,
            "common": self._make_common
        }
        make_this = choice(sample(this_item, len(this_item)))
        items = self.item_types[make_this]
        new_item = factories[make_this](choice(sample(items, len(items))))
        self.data = self._build(new_item, make_this)

    def _build(self, item_name, item_type):
        return {
            "name": item_name,
            "type": item_type,
            "description": None,
            "holder": None,
            "stats": self._get_stats(item_type)
        }

    def _make_uncommon(self, item):
        descriptor, verb = self._uncommon_desc()
        item = " ".join([descriptor, item, verb])
        return item

    def _make_common(self, item):
        desciptor = self._common_desc()
        item = " ".join([desciptor, item])
        return item

    def _uncommon_desc(self):
        verbs = self.descriptors["verbs"]        
        all_descriptors = (
            self.qualities["uncommon"] +
            self.descriptors["adjectives"] +
            self.materials
        )
        item_descriptor = choice(
            sample(all_descriptors, len(all_descriptors))
        )
        item_verb = choice(
            sample(verbs, len(verbs))
        )
        return item_descriptor, item_verb

    def _common_desc(self):
        common_qualities = self.qualities["common"]
        item_quality = choice(
            sample(common_qualities, len(common_qualities))
        )
        return item_quality

    def _get_stats(self, item_type):
        return {
            "weapon": {
                "attack": randint(10, 30),
                "weight": randint(5, 20),
                "luck": randint(5, 30)
            },
            "armor": {
                "strength": randint(10, 30),
                "weight": randint(15, 40),
                "luck": randint(5, 25)
            },
            "magic": {
                "attack": randint(15, 50),
                "amount": randint(5, 15),
                "luck": randint(5, 15)
            },
            "common": {
                "weight": randint(5, 50),
                "luck": randint(-10, 10)
            }
        }[item_type]


# def room():
#     return {
#         "description": None,
#     }


# def player():
#     return {
#         "name": None,
#         "description": None,
#     }



def yaml_writer(types, num):
    file_name = "./generic_" + types + "s.yml"
    make_this = {
        # "player": PlayerFactory,
        "item": ItemFactory,
    }[types]

    with open(file_name, "w") as save_file:
        yaml.dump(
            {i: make_this().data for i in range(num)},
            save_file,
            default_flow_style=False
        )


if __name__ == "__main__":
    yaml_writer("item", 1000)