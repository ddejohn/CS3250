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
                    population=factory_data.MATERIAL["weapon"],
                    weights=factory_data.RARITY[self.rarity],
                    k=len(factory_data.MATERIAL["weapon"])
                )
            ),
            ArmorItem: choice(
                choices(
                    population=factory_data.MATERIAL["armor"],
                    weights=factory_data.RARITY[self.rarity],
                    k=len(factory_data.MATERIAL["armor"])
                )
            )
        }[type(self).__base__]


class WeaponItem(Material):
    def __init__(self):
        super().__init__()


class ArmorItem(Material):
    def __init__(self):
        super().__init__()


class WeaponBlade(WeaponItem):
    def __init__(self):
        super().__init__()
        self.item_type = choice(["blade", "dagger", "shortsword", "longsword"])


class WeaponBow(WeaponItem):
    def __init__(self):
        super().__init__()
        self.item_type = choice(["bow", "recurve bow", "longbow", "flatbow"])


class WeaponAxe(WeaponItem):
    def __init__(self):
        super().__init__()
        self.item_type = choice(["axe", "battle axe", "labrys"])


class WeaponHammer(WeaponItem):
    def __init__(self):
        super().__init__()
        self.item_type = choice(["hammer", "war hammer", "meteor hammer"])


class ArmorChest(ArmorItem):
    def __init__(self):
        super().__init__()
        self.item_type = "armor"


class ArmorHead(ArmorItem):
    def __init__(self):
        super().__init__()
        self.item_type = "helm"


class ArmorHands(ArmorItem):
    def __init__(self):
        super().__init__()
        self.item_type = choice(["gloves", "gauntlets"])


class ArmorBoots(ArmorItem):
    def __init__(self):
        super().__init__()
        self.item_type = "boots"


if __name__ == "__main__":
    items = [
        WeaponBlade,
        WeaponAxe,
        WeaponBow,
        WeaponHammer,
        ArmorBoots,
        ArmorChest,
        ArmorHands,
        ArmorHead
    ]

    for _ in range(100):
        new_item = choice(items)()
        print(f"{new_item.rarity} {new_item.material} {new_item.item_type}")
