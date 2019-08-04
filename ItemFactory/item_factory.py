from random import choice, choices, randint
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


class WeaponName:
    def __init__(self):
        self.name = str


class WeaponStats:
    def __init__(self):
        self.damage = int
        self.range = int
        self.speed = int
        self.luck = int


class ArmorName:
    def __init__(self):
        self.name = str


class ArmorStats:
    def __init__(self):
        self.protection = int
        self.noise = int
        self.movement = int
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
        self.item_type = choice(list(factory_data.ONE_HANDED.keys()))


class WeaponTwoHand(WeaponItem):
    def __init__(self):
        super().__init__()
        self.item_type = choice(list(factory_data.TWO_HANDED.keys()))


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


from random import choice, sample
def description(item):
    conditions = shuffled(factory_data.CONDITION[item.rarity])
    adjectives = shuffled(factory_data.DETAIL_ADJECTIVE[item.rarity])
    nouns = shuffled(factory_data.DETAIL_NOUN[item.rarity])
    verbs = shuffled(factory_data.DETAIL_VERB[item.rarity])
    parts = shuffled(
        factory_data.ONE_HANDED.get(item.item_type,
            factory_data.TWO_HANDED.get(item.item_type))
    )
    made = shuffled([choice([
        "formed", "fashioned", "made", "constructed", "assembled"
    ]), verbs.pop()])
    quality = factory_data.QUALITY[item.rarity]
    with_from = choice(["with", "from", "using", "out of"])
    in_by = choice([
        "in",
        "with",
    ])
    if item.rarity in ["legendary", "mythical"]:
        all_parts = ", ".join([parts[0], parts[1], parts[2]])
        last_sentence = " ".join([
            f"\nThe {all_parts}, and {parts[3]}",
            f"are all inlaid with {inlays()}."
        ])
    else:
        last_sentence = " ".join([
            f"\nThe {is_are(parts[1])} {adjectives.pop()} and",
            f"{adjectives.pop()}, and the {is_are(parts[2])}",
            f"covered {in_by} {nouns.pop()} and {nouns.pop()}."
        ])
    
    return " ".join([
        f"{a_an(conditions.pop()).capitalize()}",
        f"{set_or_pair(item.item_type)} with",
        f"{a_an(adjectives.pop())} and {adjectives.pop()} {parts[0]},",
        f"{made.pop()} {made.pop()} {with_from}",
        f"{choice(quality)} {item.material}.",
        last_sentence
    ])

def shuffled(this):
    return sample(this, len(this))

def is_are(this):
    if this[-1] == "s" and this[-2] != "y":
        return f"{this} are"
    return f"{this} is"

def set_or_pair(this):
    if this[-1] == "s" and this[-2] != "y":
        return choice(["set", "pair"]) + f" of {this}"
    return this

def a_an(this):
    if this[0] in ["a", "e", "i", "o", "u"]:
        return f"an {this}"
    return f"a {this}"

def inlays():
    all_inlays = shuffled(factory_data.INLAYS)
    these_inlays = []
    for _ in range(randint(2, 4)):
        these_inlays.append(all_inlays.pop())
    last, *rest = these_inlays
    if rest:
        return ", ".join(rest) + f", and {last}"
    return last

if __name__ == "__main__":
    items = [
        WeaponOneHand,
        WeaponTwoHand,
        # ArmorFeet,
        # ArmorChest,
        # ArmorHands,
        # ArmorHead
    ]

    for _ in range(50):
        item = choice(items)()
        print(f"{item.rarity} {item.material} {item.item_type}:\n")
        print(description(item))
        print()
