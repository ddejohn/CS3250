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
        self.material = {
            WeaponItem: choice(
                choices(
                    population=factory_data.WEAPON_MATERIAL,
                    weights=factory_data.RARITY[self.rarity],
                    k=len(factory_data.WEAPON_MATERIAL)
                )
            ),
            ArmorItem: choice(
                choices(
                    population=factory_data.ARMOR_MATERIAL,
                    weights=factory_data.RARITY[self.rarity],
                    k=len(factory_data.ARMOR_MATERIAL)
                )
            )
        }[type(self).__base__]


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


class ArmorItem(Material):
    def __init__(self):
        super().__init__()


class WeaponOneHand(WeaponItem):
    def __init__(self):
        super().__init__()
        self.item_type = choice(list(factory_data.ONE_HANDED().keys()))
        for key, val in factory_data.item_description(self).items():
            setattr(self, key, val)


class WeaponTwoHand(WeaponItem):
    def __init__(self):
        super().__init__()
        self.item_type = choice(list(factory_data.TWO_HANDED().keys()))
        for key, val in factory_data.item_description(self).items():
            setattr(self, key, val)


class ArmorHead(ArmorItem):
    def __init__(self):
        super().__init__()
        self.item_type = "helm"


class ArmorChest(ArmorItem):
    def __init__(self):
        super().__init__()
        self.item_type = "armor"


class ArmorHands(ArmorItem):
    def __init__(self):
        super().__init__()
        self.item_type = choice(["gloves", "gauntlets"])


class ArmorFeet(ArmorItem):
    def __init__(self):
        super().__init__()
        self.item_type = "boots"


class ArmorSet:
    def __init__(self):
        self.head = ArmorHead
        self.chest = ArmorChest
        self.hands = ArmorHands
        self.feet = ArmorFeet


# class Player(Holder, ArmorSet):
#     pass


if __name__ == "__main__":
    items = [
        WeaponOneHand,
        WeaponTwoHand,
        # ArmorFeet,
        # ArmorChest,
        # ArmorHands,
        # ArmorHead
    ]

    for _ in range(1000):
        item = choice(items)()
        # if item.rarity in ["rare", "legendary", "mythical"]:
            # print(f"{item.name}:\n\n{item.description}\n")
        # if item.rarity in ["legendary", "mythical"]:
        if item.rarity == "mythical":
            print(f"{item.name}")
