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


class WeaponMaterial(Rarity):
    def __init__(self):
        super().__init__()
        self.material = choice(
            choices(
                population=factory_data.WEAPON_MATERIAL,
                weights=factory_data.RARITY[self.rarity],
                k=len(factory_data.WEAPON_MATERIAL)
            )
        )


class ArmorMaterial(Rarity):
    def __init__(self):
        super().__init__()
        self.material = {
            ArmorHeavy: choice(choices(
                population=factory_data.ARMOR_HEAVY,
                weights=factory_data.RARITY[self.rarity],
                k=len(factory_data.ARMOR_HEAVY)
            )),
            ArmorLight: choice(choices(
                population=factory_data.ARMOR_LIGHT,
                weights=factory_data.RARITY[self.rarity],
                k=len(factory_data.ARMOR_LIGHT)
            ))
        }[type(self.armor_type)]


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


class WeaponItem(WeaponMaterial):
    def __init__(self):
        super().__init__()
        self.weapon_type = choice([
            WeaponOneHand, WeaponTwoHand
        ])()


class ArmorItem(ArmorMaterial):
    def __init__(self):
        self.base_type = choice([
            ArmorHead,
            ArmorChest,
            ArmorHands,
            ArmorFeet
        ])()
        self.armor_type = choice([
            ArmorHeavy, ArmorLight
        ])(type(self.base_type))
        super().__init__()


class WeaponOneHand:
    def __init__(self):
        self.base_name = choice([
            "dagger",
            "shortsword",
            "battle axe",
            "labrys"
        ])


class WeaponTwoHand:
    def __init__(self):
        self.base_name = choice([
            "longsword",
            "recurve bow",
            "scythian bow",
            "longbow",
            "war hammer"
        ])


class ArmorHeavy:
    def __init__(self, base_type):
        self.base_name = {
            ArmorHead: choice(["helm", "helmet"]),
            ArmorChest: "cuirass",
            ArmorHands: "gauntlets",
            ArmorFeet: choice(["sabatons", "boots"])
        }[base_type]


class ArmorLight:
    def __init__(self, base_type):
        self.base_name = {
            ArmorHead: choice(["hood", "coif"]),
            ArmorChest: choice(["brigandine", "hauberk", "gambeson"]),
            ArmorHands: "gloves",
            ArmorFeet: "boots"
        }[base_type]


class ArmorHead:
    pass


class ArmorChest:
    pass


class ArmorHands:
    pass


class ArmorFeet:
    pass


class ArmorSet:
    def __init__(self):
        self.head = ArmorHead
        self.chest = ArmorChest
        self.hands = ArmorHands
        self.feet = ArmorFeet


# class Player(Holder, ArmorSet):
#     pass


# if __name__ == "__main__":
#     items = [
#         # WeaponOneHand,
#         # WeaponTwoHand,
#         ArmorHeavy,
#         ArmorLight
#     ]

#     for _ in range(10):
#         item = choice(items)()
#         # if item.rarity in ["rare", "legendary", "mythical"]:
#         # print(f"{item.name}:\n\n{item.description}\n")
#         # if item.rarity in ["legendary", "mythical"]:
#         # if item.rarity == "mythical":
#         # print(f"{item.name}")
