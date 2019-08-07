from random import choice, choices
import factory_data


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
        self.hands = int


class ArmorStats:
    def __init__(self):
        self.protection = int
        self.movement = int
        self.noise = int
        self.luck = int


class WeaponItem(Material):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.description = ""


class ArmorItem(Material):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.description = ""


class WeaponOneHand:
    def __init__(self):
        super().__init__()
        self.sub_type = self.__class__.__bases__[2]


class WeaponTwoHand:
    def __init__(self):
        super().__init__()
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
        self.base_name, self.base_sub_type = choice([
            ("recurve bow", "bow"),
            ("scythian bow", "bow"),
            ("cross bow", "bow"),
            ("longbow", "bow")
        ])


class WeaponMelee:
    def __init__(self):
        super().__init__()
        self.base_type = self.__class__.__bases__[1]
        self.base_name, self.base_sub_type = {
            WeaponOneHand: choice([
                ("dagger", "blade"),
                ("corvo", "blade"),
                ("stiletto", "blade"),
                ("blade", "blade"),
                ("shortsword", "blade"),
                ("seax", "blade"),
                ("xiphos", "blade"),
                ("baselard", "blade"),
                ("gladius", "blade"),
                ("morning star", "blunt"),
                ("mace", "blunt"),
                ("club", "blunt")
            ]),
            WeaponTwoHand: choice([
                ("longsword", "blade"),
                ("claymore", "blade"),
                ("bastard sword", "blade"),
                ("broadsword", "blade"),
                ("war scythe", "blade"),
                ("battle axe", "axe"),
                ("labrys", "axe"),
                ("halberd", "axe"),
                ("glaive", "axe"),
                ("war hammer", "blunt"),
                ("dire flail", "blunt")
            ])
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

    return type('NewItem', (item_class, item_type, item_subtype, ), {})()


if __name__ == "__main__":
    for _ in range(100):
        new_item = forge()
        # print(f"{new_item.rarity} {new_item.material} {new_item.base_name}")
        if new_item.__class__.__bases__[0] == WeaponItem:
            for key, val in factory_data.weapon_description(new_item).items():
                setattr(new_item, key, val)
            print(f"{new_item.name}:\n\n{new_item.description}\n")