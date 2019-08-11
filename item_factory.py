from random import choice, choices
import factory_data
import dictionary_print


class ItemConstruction:
    def __init__(self):
        super().__init__()
        self.item_class = choice([WeaponItem, ArmorItem])()
        self.base_type = self.item_class.base_type
        self.sub_type = type(self.base_type.sub_type).__name__
        self.base_type = type(self.base_type).__name__
        self.item_class = type(self.item_class).__name__


class BuildItem(ItemConstruction):
    def __init__(self):
        super().__init__()

    def forge(self):
        self.base_name, self.item_type = factory_data.types(self)
        self.rarity = factory_data.item_rarity()
        self.material = factory_data.item_material(self)
        self.secondary = factory_data.get_secondary(self)
        self.parts = factory_data.item_parts(self)

        construction = {
            "item_class": self.item_class,
            "base_type": self.base_type,
            "sub_type": self.sub_type,
            "base_name": self.base_name,
            "item_type": self.item_type,
            "rarity": self.rarity,
            "material": self.material,
            "secondary": self.secondary,
            "parts": self.parts
        }

        item_name_desc_stats = factory_data.build_item(self)

        item_data = {
            "name": item_name_desc_stats["name"],
            "description": item_name_desc_stats["description"],
            "stats": item_name_desc_stats["stats"],
            "construction": construction
        }

        new_item = Item()
        for key, val in item_data.items():
            setattr(new_item, key, val)

        return new_item


class Item:
    pass


class WeaponItem:
    def __init__(self):
        self.base_type = choice([WeaponOneHand, WeaponTwoHand])()


class ArmorItem:
    def __init__(self):
        self.base_type = choice([ArmorHeavy, ArmorLight])()


class WeaponOneHand:
    def __init__(self):
        self.sub_type = WeaponMelee()


class WeaponTwoHand:
    def __init__(self):
        self.sub_type = choice([WeaponMelee, WeaponRanged])()


class ArmorHeavy:
    def __init__(self):
        self.sub_type = choice([
            ArmorHead,
            ArmorChest,
            ArmorHands,
            ArmorFeet,
            # ArmorShield
        ])()


class ArmorLight:
    def __init__(self):
        self.sub_type = choice([
            ArmorHead,
            ArmorChest,
            ArmorHands,
            ArmorFeet,
            # ArmorShield
        ])()


class WeaponRanged:
    pass


class WeaponMelee:
    pass


class ArmorHead:
    pass


class ArmorChest:
    pass


class ArmorHands:
    pass


class ArmorFeet:
    pass


class ArmorShield:
    pass


if __name__ == "__main__":
    for _ in range(20):
        item = BuildItem()
        item = item.forge()
        print(dictionary_print.verbose_print(vars(item)))
