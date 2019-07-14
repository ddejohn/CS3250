import yaml
from random import sample
from random import choices
from random import choice
from random import randint
from pprint import pprint 


def _load():
    file_path = f"./new_word_bank.yml"
    with open(file_path) as file:
        data = yaml.safe_load(file.read())
    return data


def _write(make_type, make_num):
    make_this = {
        # "player": PlayerFactory,
        "item": ItemFactory,
    }[make_type]

    file_name = "./generic_" + make_type + "s.yml"
    with open(file_name, "w") as save_file:
        yaml.dump(
            {i: make_this().item for i in range(make_num)},
            save_file,
            default_flow_style=False
        )


class ItemFactory:
    print("loading data")
    data = _load()
    types = data["items"]["types"]
    condition = data["items"]["condition"]
    material = data["items"]["material"]
    posessive = data["names"]["posessive"]
    nonposessive = data["names"]["nonposessive"]
    suffixes = data["names"]["suffixes"]
    abstract = data["names"]["abstract"]
    adjectives = data["names"]["adjectives"]

    sequence = {
        "jewelry": {
            "seq": [
                [condition, material, ""],
                [adjectives, material, ""],
                [condition, material, "", abstract],
                [adjectives, "", abstract]
            ],
            "w": [15, 6, 3, 1]
        },
        "magic items": {
            "seq": [
                [condition, material, ""],
                [adjectives, material, ""],
                [condition, material, "", abstract],
                [adjectives, "", abstract]
            ],
            "w": [15, 6, 3, 1]
        },
        "magic consumables": {
            "seq": [
                [condition, "", abstract],
                [adjectives, "", abstract],
            ],
            "w": [3, 1]
        },
        "weapon": {
            "seq": [
                [condition, material, ""],
                [adjectives, ""],
                [condition, material, "", abstract],
                [adjectives, "", abstract],
                [nonposessive, suffixes],
                [posessive, suffixes],
            ],
            "w": [20, 15, 12, 10, 6, 5]
        },
        "armor": {
            "seq": [
                [condition, material, ""],
                [adjectives, ""],
                [condition, material, "", abstract],
                [adjectives, "", abstract],
            ],
            "w": [10, 6, 3, 1]
        },
        "filler": {
            "seq": [[condition, ""]],
            "w": [1]
        }
    }
    
    def __init__(self):
        item_type = choice(choices(
            population=list(self.types.keys()),
            weights=[10, 8, 3, 7, 5, 35],
            k=len(list(self.types.keys()))
        ))
        item_name = choice(choices(
            population=self.types[item_type],
            k=len(self.types[item_type])
        ))
        self.item = self.forge(item_name, item_type)

    def generate(self, item_name, item_type, unique_type, stats) -> dict:
        return {
            "name": item_name,
            "type": item_type,
            "description": unique_type,
            "stats": stats
        }

    def stats(self, item_name, item_type, unique_type) -> generate:
        stats = {
            "weapon": {
                "attack": randint(10, 30),
                "weight": randint(5, 20),
                "luck": randint(-10, 10),
            },
            "armor": {
                "strength": randint(10, 30),
                "weight": randint(15, 40),
                "luck": randint(-10, 10),
            },
            "magic": {
                "attack": randint(15, 50),
                "amount": randint(5, 15),
                "luck": randint(-10, 10),
            },
            "jewelry": {
                "strength": randint(-2,10),
                "attack": randint(-2, 10),
                "luck": randint(-4, 4),
            },
            "filler": {
                "weight": randint(5, 50),
                "luck": randint(-10, 10),
            },
            "legendary": {
                "attack": randint(60, 120),
                "weight": randint(5, 15),
                "luck": randint(20, 80),
            }
        }[item_type.split()[0]]

        return self.generate(item_name, item_type, unique_type, stats)

    def forge(self, item_name, item_type) -> stats:
        new_name = []
        unique_type = ""
        build = self.sequence[item_type]

        seq = choice(choices(
            population=build["seq"],
            weights=build["w"],
            k=len(build["seq"])
        ))

        for lists in seq:
            if isinstance(lists, dict):
                this_list = lists.get(item_type, lists.get("usable", ['']))
            elif lists:
                this_list = lists
            else:
                this_list = ['']

            this_word = choice(choices(
                population=this_list,
                k=len(this_list)
            ))

            if this_word:
                if this_word in self.suffixes:
                    new_name[-1] += this_word
                    unique_type = item_name
                    item_type = "legendary"
                else:
                    new_name.append(this_word)
            else:
                new_name.append(item_name)
        
        item_name = " ".join(new_name)
        return self.stats(item_name, item_type, unique_type)


if __name__ == "__main__":
    _write("item", 1000)
