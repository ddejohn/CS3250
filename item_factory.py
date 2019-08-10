from random import choice, choices
import factory_data
import dictionary_print


class Rarity:
    def __init__(self):
        super().__init__()
        self.rarity = choice(
            choices(
                population=list(factory_data.RARITY.keys()),
                weights=[20, 15, 10, 5, 2, 1],
                k=len(list(factory_data.RARITY.keys()))
            )
        )


class Material(Rarity):
    def __init__(self):
        super().__init__()
        self.material = self.choose(self.__class__.__bases__[1])

    def choose(self, item_type):
        material_list = {
            WeaponOneHand: factory_data.WEAPON_MATERIAL,
            WeaponTwoHand: factory_data.WEAPON_MATERIAL,
            ArmorLight: factory_data.ARMOR_LIGHT,
            ArmorHeavy: factory_data.ARMOR_HEAVY
        }[item_type]

        return choice(
            choices(
                population=material_list,
                weights=factory_data.RARITY[self.rarity],
                k=len(material_list)
            )
        )


class WeaponStats:
    def __init__(self):
        self.damage = int
        self.range = int
        self.speed = int
        self.luck = int


class ArmorStats:
    def __init__(self):
        self.protection = int
        self.movement = int
        self.noise = int
        self.luck = int


class WeaponItem(Material):
    def __init__(self):
        super().__init__()
        self.stats = WeaponStats()
        self.parts = factory_data.WEAPON_PARTS(self)
        for key, val in factory_data.item_description(self).items():
            setattr(self, key, val)
        for key, val in factory_data.weapon_stats(self).items():
            setattr(self.stats, key, val)


class ArmorItem(Material):
    def __init__(self):
        super().__init__()
        self.stats = ArmorStats()
        self.parts = factory_data.ARMOR_PARTS(self)
        for key, val in factory_data.item_description(self).items():
            setattr(self, key, val)
        for key, val in factory_data.armor_stats(self).items():
            setattr(self.stats, key, val)


class WeaponOneHand:
    def __init__(self):
        super().__init__()
        self.hands = 1
        self.sub_type = self.__class__.__bases__[2]


class WeaponTwoHand:
    def __init__(self):
        super().__init__()
        self.hands = 2
        self.sub_type = self.__class__.__bases__[2]


class ArmorHeavy:
    def __init__(self):
        super().__init__()
        self.sub_type = self.__class__.__bases__[2]


class ArmorLight:
    def __init__(self):
        super().__init__()
        self.sub_type = self.__class__.__bases__[2]


class WeaponRanged:
    def __init__(self):
        super().__init__()
        self.base_type = self.__class__.__bases__[1]
        self.base_name, self.base_sub_type = choice(
            factory_data.RANGED_WEAPONS)


class WeaponMelee:
    def __init__(self):
        super().__init__()
        self.base_type = self.__class__.__bases__[1]
        self.base_name, self.base_sub_type = {
            WeaponOneHand: choice(factory_data.ONE_HANDED_WEAPONS),
            WeaponTwoHand: choice(factory_data.TWO_HANDED_WEAPONS)
        }[self.base_type]


class ArmorHead:
    def __init__(self):
        super().__init__()
        self.base_type = self.__class__.__bases__[1]
        self.base_name = {
            ArmorHeavy: choice(["helm", "helmet"]),
            ArmorLight: choice(["hood", "coif"]),
        }[self.base_type]


class ArmorChest:
    def __init__(self):
        super().__init__()
        self.base_type = self.__class__.__bases__[1]
        self.base_name = {
            ArmorHeavy: "cuirass",
            ArmorLight: choice(["brigandine", "hauberk", "gambeson"])
        }[self.base_type]


class ArmorHands:
    def __init__(self):
        super().__init__()
        self.base_type = self.__class__.__bases__[1]
        self.base_name = {
            ArmorHeavy: "gauntlets",
            ArmorLight: "gloves"
        }[self.base_type]


class ArmorFeet:
    def __init__(self):
        super().__init__()
        self.base_type = self.__class__.__bases__[1]
        self.base_name = {
            ArmorHeavy: choice(["sabatons", "boots"]),
            ArmorLight: "boots"
        }[self.base_type]


def forge():
    types = {
        WeaponItem: [WeaponOneHand, WeaponTwoHand],
        ArmorItem: [ArmorHeavy, ArmorLight]
    }
    subtypes = {
        WeaponOneHand: [WeaponMelee],
        WeaponTwoHand: [WeaponRanged, WeaponMelee],
        ArmorHeavy: [ArmorHead, ArmorChest, ArmorHands, ArmorFeet],
        ArmorLight: [ArmorHead, ArmorChest, ArmorHands, ArmorFeet]
    }
    item_class = choice(list(types.keys()))
    item_type = choice(types[item_class])
    item_subtype = choice(subtypes[item_type])

    return type(
        "NewItem",
        (item_class, item_type, item_subtype, ),
        {"item_class": item_class}
    )()


if __name__ == "__main__":
    for _ in range(100):
        new_item = forge()
        print(f"{new_item.name}:\n\n{new_item.description}\n")
        print(dictionary_print.verbose_print(vars(new_item.stats), calls=1))
