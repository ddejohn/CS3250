from random import choices, choice, randint, shuffle
import factory_data

class ItemFactory:
    """Generates a random named item with randomized stats"""

    items = factory_data.ITEMS
    names = factory_data.NAMES
    sequence = factory_data.SEQUENCE

    types = items["types"]
    condition = items["condition"]
    material = items["material"]

    posessive = names["posessive"]
    nonposessive = names["nonposessive"]
    suffixes = names["suffixes"]
    abstract = names["abstract"]
    adjectives = names["adjectives"]

    @staticmethod
    def build(weights=None):
        """generate a random item

        Creates an item name, type, and location into game world

        Args:
            item_name (str): name of randomly generated item
            item_type (str): tpye of randomly generated item

        returns:
            item_name (str): returns the name of the randomly generated item
            item_type (str): returns the type of the randomly generated item

        """

        weights = {
            "player": [8, 0, 0, 7, 5, 10]
        # }.get(weights, [8, 35, 3, 7, 5, 10])
        }.get(weights, [8, 0, 3, 3, 5, 10])

        item_type = choice(choices(
            population=list(ItemFactory.types.keys()),
            weights=weights,
            k=len(list(ItemFactory.types.keys()))
        ))

        item_name = choice(choices(
            population=ItemFactory.types[item_type],
            k=len(ItemFactory.types[item_type])
        ))

        return ItemFactory._forge(item_name, item_type)

    @staticmethod
    def _generate(stats, item_name, item_type):
        return {
            "name": item_name,
            "type": item_type,
            "description": "",
            "stats": stats
        }

    @staticmethod
    def _stats(item_name, item_type):
        stats = factory_data.stats(item_type.split()[0])
        return ItemFactory._generate(stats, item_name, item_type)

    @staticmethod
    def _forge(item_name, item_type):
        new_name = []
        build = ItemFactory.sequence[item_type]

        seq = choice(choices(
            population=build["seq"],
            weights=build["w"],
            k=len(build["seq"])
        ))

        for lists in seq:
            if isinstance(lists, dict):
                this_list = lists.get(
                    item_type, lists.get("usable", ['']))
            elif lists:
                this_list = lists
            else:
                this_list = ['']

            this_word = choice(choices(
                population=this_list,
                k=len(this_list)
            ))

            if this_word:
                if this_word in ItemFactory.suffixes:
                    new_name[-1] += f"{this_word}"
                    item_type = f"legendary {item_name}"
                else:
                    new_name.append(this_word)
            else:
                new_name.append(item_name)

        item_name = " ".join(new_name)
        return ItemFactory._stats(item_name, item_type)


if __name__ == "__main__":
    for _ in range(1000):
        new_item = ItemFactory.build()
        if "legendary" in new_item["type"]:
            print(new_item["name"])
