import yaml
from random import sample
from random import choices
from random import randint


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
    data = _load()
    names = data["names"]
    types = data["items"]["types"]
    condition = data["items"]["condition"]
    materials = data["items"]["materials"]

    # print(types.keys())

    def __init__(self):
        self.item = dict()

    def __call__(self):
        new_item_type = choices(
            population=list(self.types.keys()),
            weights=[10, 4, 5, 25],
            k=len(list(self.types.keys()))
        )
        new_item_base_name = choices(
            population=new_item_type,
            k=len(new_item_type)
        )
        self.item = forge(new_item_base_name, new_item_type)

    def forge(self, item_name, item_type) -> stats:
        
        
        
        pass


    def stats(self, item_name, item_type) -> generate:
        pass
    
    def generate(self, item_name, item_type) -> dict:
        pass


if __name__ == "__main__":
    _write("item", 10)


# jewelry:
#     cond, material (15)
#     material, adjectives (6)
#     cond, material, abstract (3)
#     adjectives, abstract (1)
# magic:
#     cond, abstract (2)
#     adjectives, abstract (1)
# common:
#     filler
# weapon:
#     cond, material (20)
#     adjectives (15)
#     cond, material, abstract (10)
#     adjectives, abstract (6)
#     unique, nonpossessive (3)
#     unique, possessive (1)
# armor:
#     cond, material (10)
#     adjectives (6)
#     cond, material, abstract (3)
#     adjectives, abstract (1)