import numpy as np
from random import choice, choices, sample, randint, uniform


RARITY = {
    "crude":        [100, 30, 0, 0, 0, 0, 0],
    "common":       [30, 100, 30, 0, 0, 0, 0],
    "uncommon":     [0, 30, 100, 30, 0, 0, 0],
    "rare":         [0, 0, 30, 100, 30, 0, 0],
    "legendary":    [0, 0, 0, 0, 30, 100, 0],
    "mythical":     [0, 0, 0, 0, 0, 30, 100]
}


WEAPON_MATERIAL = [
    "iron",
    "steel",
    "bone",
    "obsidian",
    "electrum",
    "adamantite",
    "meteorite",
]


ARMOR_LIGHT = [
    "hide",
    "leather",
    "obsidian",
    "electrum",
    "bone",
    "adamantite",
    "meteorite"
]


ARMOR_HEAVY = [
    "iron",
    "steel",
    "obsidian",
    "bone",
    "onyx",
    "adamantite",
    "meteorite"
]


WEAPON_SECONDARY = {
    "crude": ["splintered wood", "cracked wood", "warped wood"],
    "common": ["ash", "maple"],
    "uncommon": ["beech", "mahogany", "hickory", "maple"],
    "rare": ["hickory", "birch", "cherry"],
    "legendary": ["walnut", "ebony", "bloodwood", "black oak"],
    "mythical": ["rosewood", "ebony", "black walnut", "purpleheart"]
}


ARMOR_SECONDARY = {
    "ArmorLight": [
        "lamellar",
        "scale"
    ],
    "ArmorHeavy": [
        "laminar",
        "plate"
    ]
}


INLAYS = [
    "bone",
    "gold",
    "silver",
    "onyx",
    "obsidian",
    "amethyst",
    "emerald",
    "ebony",
    "walnut",
    "ruby",
    "jade",
    "turquoise",
    "ivory",
    "bronze",
    "copper",
    "meteorite",
    "adamantite",
    "pearl"
]


LUSTERS = [
    "rainbow",
    "verdigris",
    "prismatic",
    "opalescent",
    "nacreous",
    "variegated",
    "iridescent"
]


ETCHINGS = [
    "intricate",
    "elaborate",
    "detailed",
    "elegant",
    "sophisticated",
    "complex",
    "labyrinthine",
    "minute",
]


CARVINGS = [
    "carvings",
    "etchings",
    "patterns",
    "inscriptions",
    "engravings"
]


PATINAS = [
    "patina",
    "shimmer",
    "shine",
    "sheen",
    "brilliance",
    "luster",
    "finish",
]


GLISTENS = [
    "glistens",
    "gleams",
    "glimmers",
    "twinkles",
    "flashes",
    "radiates",
    "beams",
    "glows",
    "glitters"
]


SOFT_ADJECTIVE = {
    "crude": [
        "scratched",
        "distressed",
        "chewed",
        "gnarled",
        "scored",
    ],
    "common": [
        "scratched",
        "burnished",
        "scored",
        "distressed"
    ],
}


DETAIL_ADJECTIVE = {
    "crude": [
        "scratched",
        "pitted",
        "rusted",
        "distressed",
        "chewed",
        "gnarled",
        "bent",
        "scored",
        "burred"
    ],
    "common": [
        "scratched",
        "burred",
        "burnished",
        "scored",
        "pitted",
        "rusted",
        "distressed"
    ],
    "uncommon": [
        "burnished",
        "distressed",
        "scratched",
        "worn",
        "dull",
        "rough"
    ],
    "rare": [
        "polished",
        "smooth",
        "elegant",
        "immaculate",
        "spotless"
    ],
    "legendary": [
        "ornate",
        "engraved",
        "embossed",
        "gilded",
        "elaborate"
    ],
    "mythical": [
        "ornate",
        "engraved",
        "embossed",
        "gilded",
        "elaborate"
    ]
}


DETAIL_NOUN = {
    "crude": [
        "dried blood",
        "dirt",
        "dust",
        "claw marks",
        "scratches",
        "gashes",
        "notches",
        "bits of fur",
        "teeth marks"
    ],
    "common": [
        "dried blood",
        "dirt",
        "claw marks",
        "scratches",
        "filth",
        "smudges",
    ],
    "uncommon": [
        "smudges",
        "grit",
        "scratches",
        "soot",
        "residue"
    ],
    "rare": [],
    "legendary": [],
    "mythical": []
}


DETAIL_VERB = {
    "crude": [
        "haphazardly",
        "shoddily",
        "crudely",
        "defectively",
        "inexpertly",
        "poorly",
        "hastily"
    ],
    "common": [
        "haphazardly",
        "hastily",
        "inexpertly",
        "adequately",
        "competently"
    ],
    "uncommon": [
        "adequately",
        "competently",
        "sufficiently",
        "decently",
        "capably"
    ],
    "rare": [
        "meticulously",
        "skillfully",
        "precisely",
        "diligently",
        "fastidiously"
    ],
    "legendary": [
        "expertly",
        "elegantly",
        "masterfully",
        "flawlessly"
    ],
    "mythical": [
        "expertly",
        "elegantly",
        "masterfully",
        "flawlessly"
    ]
}


CONDITION = {
    "crude": [
        "ruined",
        "rusty",
        "marred",
        "deformed",
        "lousy",
        "mediocre",
        "dreadful",
        "inferior",
        "substandard",
        "tarnished",
        "blighted",
        "filthy",
        "decrepit"
    ],
    "common": [
        "worn",
        "chipped",
        "blemished",
        "flawed",
        "mediocre",
        "common",
        "middling",
        "tarnished",
        "neglected",
        "mended"
    ],
    "uncommon": [
        "fair",
        "passable",
        "acceptable",
        "adequate",
        "blemished",
        "tarnished",
        "mended"
    ],
    "rare": [
        "fine",
        "exceptional",
        "refined",
        "superior",
        "unblemished",
        "faultless",
        "pristine"
    ],
    "legendary": [
        "flawless",
        "immaculate",
        "pristine",
        "exquisite",
        "superior",
        "refined",
        "impeccable",
        "superb"
    ],
    "mythical": [
        "flawless",
        "immaculate",
        "pristine",
        "exquisite",
        "superior",
        "refined",
        "impeccable"
    ]
}


NAMES = {
    "abstract": [
        "of blooding",
        "of humiliation",
        "of hubris",
        "of spite",
        "of death",
        "of life",
        "of regret",
        "of dread",
        "of sorrow",
        "of screams",
        "of lust",
        "of carving",
        "of surprise",
        "of confusion",
        "of frenzy",
        "of breaking",
        "of loathing",
        "of sickness",
        "of poisons",
        "of tragedy",
        "of souls",
        "of rotting",
        "of governing",
        "of ecstasy",
        "of torpor",
        "of truth",
        "of lies",
        "of victory",
        "of ambition",
        "of vengeance",
        "of somnolence",
        "of joy",
        "of corruption",
        "of erosion",
        "of jubilance",
        "of merit",
        "of witching",
        "of burdens",
        "of honor",
        "of repulsion",
        "of reckoning",
        "of mourning",
        "of grieving",
        "of judgement",
        "of battering",
        "of hell",
        "of starlight",
        "of scorching",
        "of smite",
        "of waning",
        "of smiting",
        "of diffusion",
        "of mummification",
        "of crushing",
        "of extraction",
        "of valor",
        "of fear",
        "of firestorms",
        "of icestorms",
        "of ice",
        "of thunder",
        "of lightning",
        "of hatred",
        "of terror",
        "of ruin",
        "of storms",
        "of ruining",
        "of fury",
        "of disgust",
        "of friendship",
        "of calming",
        "of shame",
        "of pity",
        "of envy",
        "of suffering",
        "of tears",
        "of disdain",
        "of putrification",
        "of contempt",
        "of mediocrity",
        "of misery",
        "of thorns",
        "of light",
        "of dark",
        "of darkness",
        "of dawn",
        "of dusk",
        "of herecy",
        "of twilight",
        "of maleficence",
        "of brutality",
        "of savagery",
        "of malice",
        "of quickening",
        "of grace",
        "of disintegration",
        "of disintegrating",
        "of embalming",
        "of destruction",
        "of exsanguination",
        "of the hunt",
        "of the grotesque",
        "of the heretic",
        "of the prophet",
        "of the night",
        "of the stars",
        "of the storm",
        "of the shamed",
        "of the hated",
        "of the dawn",
        "of the dusk",
        "of the morning"
    ],
    "adjectives": [
        "ghastly",
        "addictive",
        "gilded",
        "beautiful",
        "valorous",
        "ancient",
        "magnificent",
        "strange",
        "dreaded",
        "fearful",
        "splendid",
        "horrible",
        "luminous",
        "furious",
        "shameful",
        "friendly",
        "piteous",
        "weeping",
        "splendiferous",
        "loathsome",
        "blunderous",
        "magnetic",
        "electric",
        "burning",
        "brutal",
        "savage",
        "graceful",
        "volcanic",
        "uncanny",
        "spectral",
        "sinister",
        "ornate",
        "bloody",
        "ashen",
        "gleaming",
        "glittering",
        "eldritch",
        "eerie",
        "elegant",
        "exquisite",
        "munificent",
        "mirthful",
        "noxious",
        "nefarious",
        "repulsive",
        "freakish",
        "bewitched",
        "repugnant",
        "exotic",
        "burdensome",
        "vigilant",
        "bewildering",
        "chosen",
        "dazzling",
        "dusky",
        "putrid",
        "unpleasant",
        "bizarre",
        "frenzied",
        "stormy",
        "erosive",
        "vengeful",
        "somnolent",
        "opulent",
        "lustrous",
        "hideous",
        "insideous",
        "spiteful",
        "ugly",
        "thorny",
        "barbed",
        "ghoulish",
        "soulless",
        "corrupted",
        "envious",
        "grotesque",
        "weeping"
    ],
    "prefixes": [
        "wolf",
        "troll",
        "goliath",
        "raven",
        "dragon",
        "crow",
        "widow",
        "thorn",
        "wraith",
        "spine",
        "doom",
        "death",
        "hate",
        "bone",
        "fear",
        "soul",
        "sky",
        "mind",
        "god",
        "star",
        "shadow",
        "sun",
        "moon",
        "storm"
    ],
    "verbs": [
        "ripper",
        "eater",
        "stealer",
        "absorber",
        "shredder",
        "bruiser",
        "seer",
        "destroyer",
        "killer",
        "purger",
        "bearer",
        "corruptor",
        "preacher",
        "defier",
        "husher",
        "defiler",
        "dredger",
        "mutilator",
        "adder",
        "breaker",
        "scorcher",
        "maker",
        "bringer",
        "slayer"
    ],
    "nouns": [
        "eye",
        "fang",
        "claw",
        "bane",
        "marrow",
        "thorn",
        "heart",
        "blood",
        "wail",
        "tooth"
    ]
}


WEAPON_STAT_DATA = {
    "WeaponMelee": {
        "WeaponOneHand": {
            "crude": [6, 4, 4, 2],
            "common": [10, 4, 8, 4],
            "uncommon": [20, 4, 8, 6],
            "rare": [30, 4, 8, 8],
            "legendary": [50, 6, 10, 10],
            "mythical": [80, 8, 12, 12]
        },
        "WeaponTwoHand": {
            "crude": [12, 8, 2, 2],
            "common": [18, 8, 4, 4],
            "uncommon": [28, 8, 4, 4],
            "rare": [42, 8, 6, 8],
            "legendary": [68, 10, 8, 10],
            "mythical": [100, 12, 10, 12]
        }
    },
    "WeaponRanged": {
        "WeaponTwoHand": {
            "crude": [10, 10, 4, 4],
            "common": [16, 18, 4, 4],
            "uncommon": [20, 20, 6, 6],
            "rare": [40, 24, 6, 6],
            "legendary": [50, 30, 8, 8],
            "mythical": [80, 45, 12, 10]
        }
    }
}


ARMOR_STAT_DATA = {
    "stats": {
        # protection movement noise luck
        "crude":        [4, 1, 5, 1],
        "common":       [8, 1, 3, 2],
        "uncommon":     [10, 0.5, 2, 4],
        "rare":         [14, 0.125, 0.5, 5],
        "legendary":    [20, 0.025, 0.05, 12],
        "mythical":     [40, 0.0125, 0.025, 16]
    },
    "mults": {
        # protection movement noise luck
        "ArmorHead":    [1, -1, 0.5, 1],
        "ArmorChest":   [3, -1.5, 1.5, 1],
        "ArmorHands":   [0.5, -0.5, 0.5, 1],
        "ArmorFeet":    [1.5, -0.5, 0.25, 1]
    }
}


def types(item):
    return {
        "WeaponOneHand": {
            "WeaponMelee": choice([
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
        },
        "WeaponTwoHand": {
            "WeaponMelee": choice([
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
            ]),
            "WeaponRanged": choice([
                ("recurve bow", "bow"),
                ("scythian bow", "bow"),
                ("cross bow", "bow"),
                ("longbow", "bow")
            ])
        },
        "ArmorHeavy": {
            "ArmorHead": (choice(["helm", "helmet"]), "heavy head"),
            "ArmorChest": ("cuirass", "heavy chest"),
            "ArmorHands": ("gauntlets", "heavy hands"),
            "ArmorFeet": (choice(["sabatons", "boots"]), "heavy feet"),
            "ArmorShield": (
                choice(["pavise shield", "kite shield"]), "heavy shield"
            )
        },
        "ArmorLight": {
            "ArmorHead": (choice(["hood", "coif"]), "light head"),
            "ArmorChest": (
                choice(["brigandine", "hauberk", "gambeson"]), "light chest"
            ),
            "ArmorHands": ("gloves", "light hands"),
            "ArmorFeet": ("boots", "light feet"),
            "ArmorShield": (
                choice(["buckler shield", "targe shield"]), "light shield"
            )
        }
    }[item.base_type][item.sub_type]


def item_rarity():
    return choice(
        choices(
            population=list(RARITY.keys()),
            weights=[20, 15, 10, 5, 2, 1],
            k=len(list(RARITY.keys()))
        )
    )


def item_material(item):
    material_list = {
        "WeaponOneHand": WEAPON_MATERIAL,
        "WeaponTwoHand": WEAPON_MATERIAL,
        "ArmorLight": ARMOR_LIGHT,
        "ArmorHeavy": ARMOR_HEAVY
    }[item.base_type]

    return choice(
        choices(
            population=material_list,
            weights=RARITY[item.rarity],
            k=len(material_list)
        )
    )


def item_parts(item):
    return {
        "blade": [
            "fuller",
            "pommel",
            choice(["hilt", "grip"]),
            choice(["cross-guard", "quillon"])
        ],
        "axe": [
            "pommel",
            "haft",
            "hook",
            "beard"
        ],
        "bow": [
            "nock",
            "face",
            choice(["hilt", "grip"])
        ],
        "blunt": [
            "throat",
            choice(["cheek", "flange"]),
            choice(["face", "crown"]),
            choice(["haft", "handle", "grip"])
        ],
        "heavy head": [
            "visor",
            "comb",
            choice(["gorget", "aventail", "camail"])
        ],
        "light head": [
            "cowl",
            "gaiter",
            "closure"
        ],
        "heavy chest": [
            "breastplate",
            "pauldrons",
            "faulds",
            "gardbrace",
            "bassart"
        ],
        "light chest": [
            "plackard",
            "spaulders",
            "gardbrace",
            "culet",
        ],
        "heavy hands": [
            "rerebraces",
            choice(["lower cannons", "vambraces"]),
            choice(["carpal plates", "wrist plates"]),
            "cuffs"
        ],
        "light hands": [
            "rerebraces",
            choice(["lower cannons", "vambraces"]),
            choice(["carpal plates", "wrist plates"]),
            "cuffs"
        ],
        "heavy feet": [
            "cuisse",
            "greaves",
            "solleret"
        ],
        "light feet": [
            "cuisse",
            "greaves",
            "sabatons"
        ],
        "heavy shield": [],
        "light shield": []
    }[item.item_type]


def build_item(item):
    condition = shuffled(CONDITION[item.rarity])
    adjective = shuffled(DETAIL_ADJECTIVE[item.rarity])
    noun = shuffled(DETAIL_NOUN[item.rarity])
    verb = shuffled(DETAIL_VERB[item.rarity])
    parts = shuffled(item.parts)
    pops = shuffled([0, 1, 2])
    in_by = choice(["in", "with", "by"])
    made = choice([
        "shaped",
        "formed",
        "fashioned",
        "made",
        "constructed",
        "assembled"
    ])
    construction = {
        "WeaponItem": f"{item.material} and {item.secondary}",
        "ArmorItem": f"{item.secondary}{item.material}"
    }[item.item_class]
    item_stats = {
        "WeaponItem": weapon_stats,
        "ArmorItem": armor_stats
    }[item.item_class](item)

    def leathers(item):
        soft_adjectives = shuffled(SOFT_ADJECTIVE[item.rarity])
        qualities = f"{soft_adjectives.pop()} and {soft_adjectives.pop()}"
        last, *rest = parts
        rest = ", ".join(rest)
        
        
        last_sentence = " ".join([
            f"The {rest}, and {last}",
            f"are all covered {in_by} {noun.pop()} and {noun.pop()}."
        ])

        first_sentence = " ".join([
            f"{(a_an(soft_adjectives.pop()).capitalize())}",
            f"{set_or_pair(item.base_name)} {verb.pop()} {made}",
            f"from {qualities} {construction}."
        ])

        return f"{first_sentence} {last_sentence}"

    if item.material in ["hide", "leather"]:
        if item.rarity in ["crude", "common", "uncommon"]:
            chosen_name = choice([
                [item.rarity, item.material, item.base_name],
                [
                    choice(SOFT_ADJECTIVE[item.rarity]),
                    item.material,
                    item.base_name
                ]
            ])
            new_name = " ".join(chosen_name)
        else:
            new_name = hood_name(item)
        return {
            "name": new_name,
            "description": leathers(item),
            "stats": item_stats
        }

    first_sentence = " ".join([
        f"{a_an(condition.pop()).capitalize()}",
        f"{set_or_pair(item.base_name)} with",
        f"{a_an(adjective.pop(), adjective.pop(), parts[pops.pop()])},",
        f"{verb.pop()} {made} from {construction}."
    ])

    if item.rarity == "rare":
        last, *rest = parts
        rest = ", ".join(rest)
        last_sentence = " ".join([
            f"The {rest}, and {last}",
            f"are all covered in {patinas_etchings(item.base_name)}."
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
            f"The {is_are(parts[pops.pop()])} {adjective.pop()} and",
            f"{adjective.pop()}, and the {is_are(parts[pops.pop()])}",
            f"covered {in_by} {noun.pop()} and {noun.pop()}."
        ])

    if item.rarity in ["crude", "common", "uncommon"]:
        chosen_name = choice([
            [item.rarity, item.material, item.base_name],
            [choice(CONDITION[item.rarity]), item.material, item.base_name]
        ])
        new_name = " ".join(chosen_name)
    elif item.item_class == "ArmorItem":
        new_name = hood_name(item)
    else:
        new_name = item_name(item)

    return {
        "name": new_name,
        "description": f"{first_sentence} {last_sentence}",
        "stats": item_stats
    }


def hood_name(item):
    adjectives = NAMES["adjectives"]
    abstract = NAMES["abstract"]
    new_name = []
    if item.rarity == "rare":
        new_name.extend(choice([
            [choice(adjectives), item.material, item.base_name],
            [
                choice(CONDITION[item.rarity]),
                item.material,
                item.base_name,
                choice(abstract)
            ]
        ]))
    elif item.rarity in ["legendary", "mythical"]:
        new_name.extend(choice([
            [choice(adjectives), item.base_name, choice(abstract)],
            [
                choice(adjectives),
                item.material,
                item.base_name,
                choice(abstract)
            ]
        ]))

    return " ".join(new_name)


def item_name(item):
    adjectives = NAMES["adjectives"]
    abstract = NAMES["abstract"]
    prefixes = NAMES["prefixes"]
    verbs = NAMES["verbs"]
    nouns = NAMES["nouns"]
    new_name = []

    if item.rarity == "rare":
        new_name.extend(choice([
            [choice(adjectives), item.material, item.base_name],
            [
                choice(CONDITION[item.rarity]),
                item.material,
                item.base_name,
                choice(abstract)
            ]
        ]))
    elif item.rarity == "legendary":
        new_name.extend(choice([
            [choice(adjectives), item.base_name, choice(abstract)],
            [
                choice(adjectives),
                item.material,
                item.base_name,
                choice(abstract)
            ],
            [choice(adjectives), choice(nouns), choice(abstract)],
            [choice(adjectives), item.material, choice(nouns)],
            [choice(adjectives), choice(nouns), "of " + item.material],
            [
                choice(adjectives),
                item.material,
                choice(nouns),
                choice(abstract)
            ]
        ]))
    else:
        new_name.extend(choice([
            [choice(prefixes), choice(verbs)],
            [choice(prefixes)+"'s", choice(nouns)],
            [choice(prefixes)+"'s", choice(adjectives), choice(nouns)],
            [choice(adjectives), choice(nouns), choice(abstract)]
        ]))

    return " ".join(new_name)


def weapon_stats(item):
    stats = WEAPON_STAT_DATA[item.sub_type][item.base_type][item.rarity]
    stats = [round(stdev(x), ndigits=2) for x in stats]

    return {
        "damage": stats[0],
        "range": stats[1],
        "speed": stats[2],
        "luck": stats[3]
    }


def armor_stats(item):
    stats = ARMOR_STAT_DATA["stats"][item.rarity]
    mults = ARMOR_STAT_DATA["mults"][item.sub_type]
    wt = {
        "ArmorHeavy": 2,
    }.get(item.base_type, 1)
    combs = [round(wt*stdev(x*y), ndigits=2) for x, y in zip(stats, mults)]

    return {
        "protection": combs[0],
        "movement": combs[1],
        "noise": combs[2],
        "luck": combs[3]
    }


def get_secondary(item):
    return {
        "WeaponItem": weapon_construction,
        "ArmorItem": armor_construction
    }[item.item_class](item)


def weapon_construction(item):
    return choice(WEAPON_SECONDARY[item.rarity])


def armor_construction(item):
    if item.rarity not in ["crude", "common"]:
        return f"{choice(ARMOR_SECONDARY[item.base_type])} "
    return f""


def shuffled(this):
    return sample(this, len(this))


def is_are(this):
    if this[-1] == "s" and this[-2] != "y":
        return f"{this} are"
    return f"{this} is"


def set_or_pair(this):
    if this[-1] == "s" and this[-2] != "y" and this[-2:] != "ss":
        return choice(["set", "pair"]) + f" of {this}"
    return this


def a_an(*this):
    first, *rest = this
    if rest:
        rest = " ".join(rest)
        if " " in rest:
            rest = f" and {rest}"
        else:
            rest = f" {rest}"
    else:
        rest = ""
    if rest and rest[-1] == "s":
        return f"{first}{rest}"
    elif first[0] in ["a", "e", "i", "o", "u"]:
        return f"an {first}{rest}"
    return f"a {first}{rest}"


def inlays():
    all_inlays = shuffled(INLAYS)
    these_inlays = []
    for _ in range(randint(1, 3)):
        these_inlays.append(all_inlays.pop())
    last, *rest = these_inlays
    if rest:
        if len(rest) == 1:
            return f"{last} and {rest.pop()}"
        return ", ".join(rest) + f", and {last}"
    return last


def patinas_etchings(base_name):
    if base_name in ["morning star", "dire flail"]:
        general_name = "weapon"
    else:
        general_name = base_name.split()[-1]
    if base_name[-1] == "s":
        second_sentence = base_name
        glisten_choice = choice(GLISTENS).rstrip("s")
    else:
        second_sentence = f"{choice(['whole', 'entire'])} {general_name}"
        glisten_choice = choice(GLISTENS)
    return " ".join([
        f"{choice(ETCHINGS)} {choice(CARVINGS)},",
        f"and the {second_sentence}",
        glisten_choice,
        f"with {a_an(choice(LUSTERS))}",
        f"{choice(PATINAS)}"
    ])


def stdev(x):
    return uniform(x-0.3*x, x+0.3*x)
