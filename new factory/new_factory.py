import new_factory_data

class ItemFactory:

    items = new_factory_data.ITEMS
    names = new_factory_data.NAMES
    sequence = new_factory_data.SEQUENCE

    types = items["types"]
    condition = items["condition"]
    material = items["material"]

    posessive = names["posessive"]
    nonposessive = names["nonposessive"]
    suffixes = names["suffixes"]
    abstract = names["abstract"]
    adjectives = names["adjectives"]

    build_switch = {
        "weapon": WeaponBuilder,
        "armor": ArmorBuilder,
        "magic": MagicBuilder,
        "potion": PotionBuilder,
        "jewelry": JewelryBuilder,
    }



def BuilderClass(X):
    class BuilderType(X):
        def __init__(self):
            super().__init__()
    return BuilderType


class WeaponBuilder(ItemFactory):
    pass


class ArmorBuilder(ItemFactory):
    pass


class MagicBuilder(ItemFactory):
    pass


class PotionBuilder(ItemFactory):
    pass


class JewelryBuilder(ItemFactory):
    pass


class StatsBuilder(X):
    pass