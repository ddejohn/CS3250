from random import choice, sample, randint
import factory_data


def description(item):
    condition = shuffled(factory_data.CONDITION[item.rarity])
    adjective = shuffled(factory_data.DETAIL_ADJECTIVE[item.rarity])
    secondary = shuffled(factory_data.WEAPON_SECONDARY[item.rarity])
    noun = shuffled(factory_data.DETAIL_NOUN[item.rarity])
    verb = shuffled(factory_data.DETAIL_VERB[item.rarity])
    parts = shuffled(
        factory_data.ONE_HANDED().get(item.item_type,
            factory_data.TWO_HANDED().get(item.item_type))
    )
    made = choice([
        "shaped",
        "formed",
        "fashioned",
        "made",
        "constructed",
        "assembled"
    ])
    in_by = choice(["in", "with", "by"])
    
    first_sentence = " ".join([
        f"{a_an(condition.pop()).capitalize()}",
        f"{set_or_pair(item.item_type)} with",
        f"{a_an(adjective.pop())} and {adjective.pop()} {parts.pop()},",
        f"{verb.pop()} {made} from",
        f"{item.material} and {choice(secondary)}.",
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
            f"The {is_are(parts.pop())} {adjective.pop()} and",
            f"{adjective.pop()}, and the {is_are(parts.pop())}",
            f"covered {in_by} {noun.pop()} and {noun.pop()}."
        ])
    
    return f"{first_sentence}\n{last_sentence}"

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