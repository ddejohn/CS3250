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
        self.item_type = choice(list(factory_data.ONE_HANDED().keys()))


class WeaponTwoHand(WeaponItem):
    def __init__(self):
        super().__init__()
        self.item_type = choice(list(factory_data.TWO_HANDED().keys()))


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
        factory_data.ONE_HANDED().get(item.item_type,
            factory_data.TWO_HANDED().get(item.item_type))
    )
    made = shuffled([choice([
        "formed", "fashioned", "made", "constructed", "assembled"
    ]), verbs.pop()])
    quality = factory_data.QUALITY[item.rarity]
    with_from = choice(["with", "from", "out of"])
    in_by = choice([
        "in",
        "with",
    ])
    
    first_sentence = " ".join([
        f"{a_an(conditions.pop()).capitalize()}",
        f"{set_or_pair(item.item_type)} with",
        f"{a_an(adjectives.pop())} and {adjectives.pop()} {parts.pop()},",
        f"{made.pop()} {made.pop()} {with_from}",
        f"{choice(quality)} {item.material}.",
    ])

    if item.rarity == "rare":
        last, *rest = parts
        rest = ", ".join(rest)
        last_sentence = " ".join([
            f"The {rest}, and {last}",
            f"are all covered in {patinas_etchings(item.item_type)}."
        ])
    elif item.rarity in ["legendary", "mythical"]:
        last, *rest = parts
        rest = ", ".join(rest)
        last_sentence = " ".join([
            f"The {rest}, and {last}",
            f"are all inlaid with {inlays()}."
        ])
    else:
        last_sentence = " ".join([
            f"The {is_are(parts.pop())} {adjectives.pop()} and",
            f"{adjectives.pop()}, and the {is_are(parts.pop())}",
            f"covered {in_by} {nouns.pop()} and {nouns.pop()}."
        ])
    
    return f"{first_sentence} {last_sentence}"

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
    for _ in range(randint(1, 3)):
        these_inlays.append(all_inlays.pop())
    last, *rest = these_inlays
    if rest:
        if len(rest) == 1:
            return f"{last} and {rest[0]}"
        return ", ".join(rest) + f", and {last}" 
    return last

def patinas_etchings(item_type):
    return " ".join([
        f"{choice(factory_data.ETCHINGS)} {choice(factory_data.CARVINGS)},",
        f"and the {choice(['whole', 'entire'])} {item_type.split()[-1]}",
        f"{choice(factory_data.GLISTENS)}",
        f"with {a_an(choice(factory_data.LUSTERS))}",
        f"{choice(factory_data.PATINAS)}"
    ])

if __name__ == "__main__":
    items = [
        WeaponOneHand,
        WeaponTwoHand,
        # ArmorFeet,
        # ArmorChest,
        # ArmorHands,
        # ArmorHead
    ]
    from pprint import pprint
    for _ in range(50):
        item = choice(items)()
        print(f"{item.rarity} {item.material} {item.item_type}:\n")
        print(description(item))
        print()
