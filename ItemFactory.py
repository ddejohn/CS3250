from random import choices, choice
import factory_data


class ItemFactory:
    """"""

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

    def __init__(self):
        self.item_name = str
        self.item_type = str

    def __call__(self, weights=None):
        weights = {
            "player": [8, 0, 0, 7, 5, 10]
        }.get(weights, [8, 35, 3, 7, 5, 10])

        self.item_type = choice(choices(
            population=list(self.types.keys()),
            weights=weights,
            k=len(list(self.types.keys()))
        ))

        self.item_name = choice(choices(
            population=self.types[self.item_type],
            k=len(self.types[self.item_type])
        ))

        return self.forge()

    def generate(self, unique_type, stats) -> dict:
        return {
            "name": self.item_name,
            "type": self.item_type,
            "description": unique_type,
            "stats": stats
        }

    def stats(self, unique_type) -> generate:
        stats = factory_data.stats(self.item_type.split()[0])
        return self.generate(unique_type, stats)

    def forge(self) -> stats:
        new_name = []
        unique_type = ""
        build = self.sequence[self.item_type]

        seq = choice(choices(
            population=build["seq"],
            weights=build["w"],
            k=len(build["seq"])
        ))

        for lists in seq:
            if isinstance(lists, dict):
                this_list = lists.get(
                    self.item_type, lists.get("usable", ['']))
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
                    unique_type = self.item_name
                    self.item_type = "legendary"
                else:
                    new_name.append(this_word)
            else:
                new_name.append(self.item_name)

        self.item_name = " ".join(new_name)
        return self.stats(unique_type)


if __name__ == "__main__":
    fac = ItemFactory()
    d = {}
    for i in range(5):
        d[i] = fac()

    print(d)
