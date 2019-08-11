from random import choice, choices, sample, uniform, randint


#——————————————————————————————— build sequence ——————————————————————————————#


def new_item():
    item_class, base_type, sub_type, *item_type = choice([
        "weapon " + choice([
            "melee " + choice([
                "one-handed ",
                "two-handed "
            ]) + choice([
                "blade",
                "axe",
                "blunt"
            ]),
            "ranged two-handed bow"
        ]),
        "armor " + choice([
            "heavy ",
            "light "
        ]) + choice([
            "head",
            "chest",
            "hands",
            "feet",
            "shield"
        ])
    ]).split()

    if not item_type:
        item_type = " ".join([base_type, sub_type])
    else:
        item_type = item_type.pop()
    return item_class, base_type, sub_type, item_type


def base_name(item):
    return {
        "weapon": {
            "one-handed": {
                "melee": {
                    "axe": choice([
                        "labrys",
                        "hatchet"
                    ]),
                    "blunt": choice([
                        "morning star",
                        "mace",
                        "club",
                        "flail"
                    ]),
                    "blade": choice([
                        "dagger",
                        "corvo",
                        "stiletto",
                        "shortsword",
                        "seax",
                        "xiphos",
                        "baselard",
                        "gladius"
                    ])
                }
            },
            "two-handed": {
                "melee": {
                    "blunt": choice([
                        "war hammer",
                        "meteor hammer",
                        "dire flail"
                    ]),
                    "blade": choice([
                        "longsword",
                        "claymore",
                        "broadsword",
                        "bastard sword",
                        "war scythe"
                    ]),
                    "axe": choice([
                        "battle axe",
                        "halberd",
                        "glaive"
                    ])
                },
                "ranged": {
                    "bow": choice([
                        "recurve bow",
                        "scythian bow",
                        "crossbow",
                        "longbow"
                    ])
                }
            }
        },
        "armor": {
            "head": {
                "heavy": {
                    "heavy head": choice(["helm", "helmet"])
                },
                "light": {
                    "light head": choice(["hood", "coif"])
                }
            },
            "chest": {
                "heavy": {
                    "heavy chest": choice(["cuirass", "corslet"])
                },
                "light": {
                    "light chest": choice(["brigandine", "gambeson"])
                }
            },
            "hands": {
                "heavy": {
                    "heavy hands": "gauntlets"
                },
                "light": {
                    "light hands": "gloves"
                }
            },
            "feet": {
                "heavy": {
                    "heavy feet": choice(["boots", "sabatons"])
                },
                "light": {
                    "light feet": "boots"
                }
            },
            "shield": {
                "heavy": {
                    "heavy shield": choice(["pavise shield", "kite shield"])
                },
                "light": {
                    "light shield": choice(["buckler", "targe shield"])
                }
            }
        }
    }[item.item_class][item.sub_type][item.base_type][item.item_type]


def item_rarity():
    rarities = {
        "crude":        [100, 30, 0, 0, 0, 0, 0],
        "common":       [30, 100, 30, 0, 0, 0, 0],
        "uncommon":     [0, 30, 100, 30, 0, 0, 0],
        "rare":         [0, 0, 30, 100, 30, 0, 0],
        "legendary":    [0, 0, 0, 0, 30, 100, 0],
        "mythical":     [0, 0, 0, 0, 0, 30, 100]
    }
    rarity = _choose(rarities.keys(), [20, 15, 10, 5, 2, 1])
    material_weights = rarities[rarity]
    return rarity, material_weights


def item_material(item):
    material_list = {
        "heavy": HEAVY_ARMOR_MATERIAL,
        "light": LIGHT_ARMOR_MATERIAL
    }.get(item.base_type, WEAPON_MATERIAL)

    return _choose(material_list, item.material_weights)


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
            "tasset"
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
    }[item.sub_type]


def get_secondary(item):
    return {
        "weapon": _weapon_secondary,
        "armor": _armor_construction
    }[item.item_class](item)


#—————————————————————————————————— helpers ——————————————————————————————————#


def _weapon_secondary(item):
    return choice(WEAPON_SECONDARY[item.rarity])


def _armor_construction(item):
    if item.rarity not in ["crude", "common"]:
        return f"{choice(ARMOR_CONSTRUCTION[item.base_type])} "
    return f""


def _choose(ppl, wts):
    return choice(choices(population=ppl, weights=wts, k=len(ppl)))


def shuffled(ppl):
    return sample(ppl, len(ppl))


def variance(x):
    return uniform(x-0.3*x, x+0.3*x)


def is_are(this):
    if " " in this or (this[-1] == "s" and this[-2] != "y"):
        return f"{this} are"
    return f"{this} is"


def set_or_pair(this):
    if this[-1] == "s" and this[-2] not in ["s", "y"]:
        return choice(["set", "pair"]) + f" of {this}"
    return this


def a_an(*this):
    first, *rest = this
    rest = " ".join(rest)

    if " " in rest:
        rest = f"and {rest}"
    else:
        rest = ""

    if not rest:
        return first
    elif rest[-1] == "s":
        return f"{first} {rest}"
    elif first[0] in ["a", "e", "i", "o", "u"]:
        return f"an {first} {rest}"
    return f"a {first} {rest}"


def listify_words(this):
    *rest, last = this
    rest = ", ".join(rest)
    if rest:
        if len(rest) == 1:
            return f"{rest} and {last}"
        return f"{rest}, and {last}"
    return last


#———————————————————————————————— description ————————————————————————————————#


def item_description(item):
    condition = shuffled(CONDITION[item.rarity])
    adj = shuffled(ADJECTIVES)
    pops = shuffled([0, 1, 2])
    in_by = choice(["in", "with", "by"])
    construction = {
        "weapon": f"{item.material} and {item.secondary}",
        "armor": f"{item.secondary}{item.material}"
    }[item.item_class]

    if item.material in ["hide", "leather"]:
        return soft_description(item, construction, in_by)
    return " ".join([
        f"{(a_an(condition.pop()).capitalize())}",
        f"{set_or_pair(item.base_name)} with",
        f"{a_an(adj.pop(), adj.pop(), item.parts[pops.pop()])},",
        f"{shuffled(DETAIL_VERB[item.rarity]).pop()}",
        f"{get_make()} from {construction}.",
        get_details(item)
    ])


def soft_description(item, construction, in_by):
    verbs = shuffled(DETAIL_VERB[item.rarity])
    nouns = shuffled(DETAIL_NOUN[item.rarity])
    soft_adjectives = shuffled(SOFT_ADJECTIVE[item.rarity])
    qualities = f"{soft_adjectives.pop()} and {soft_adjectives.pop()}"
    return " ".join([
        f"{(a_an(soft_adjectives.pop()).capitalize())}",
        f"{set_or_pair(item.base_name)} {verbs.pop()}",
        f"{get_make()} from {qualities} {construction}.",
        f"The {listify_words(item.parts)} are all covered {in_by}",
        f"{nouns.pop()} and {nouns.pop()}."
    ])


def inlays(item):
    k = {"rare": 1, "legendary": 2, "mythical": 4}[item.rarity]
    if k == 4:
        parts = shuffled(item.parts)
        inlays = sample(INLAYS, k)
        parts_one, parts_two = parts[:2], parts[2:]
        inlays_one, inlays_two = inlays[:2], inlays[2:]
        all_inlays = " ".join([
            f"The {is_are(listify_words(parts_one))}",
            f"inlaid with {listify_words(inlays_one)},",
            f"and the {is_are(listify_words(parts_two))} decorated with",
            f"{listify_words(inlays_two)} insets."
        ])
    else:
        all_inlays = " ".join([
            f"The {listify_words(item.parts)} are all inlaid with",
            f"{listify_words(sample(INLAYS, k))}."
        ])
    return all_inlays


def patinas_etchings(item):
    if item.base_name in ["morning star", "dire flail", "flail"]:
        general_name = "weapon"
    else:
        general_name = item.base_name.split()[-1]
    if item.base_name[-1] == "s":
        second_sentence = item.base_name
        glisten_choice = choice(GLISTENS_VERB).rstrip("s")
    else:
        second_sentence = f"{choice(['whole', 'entire'])} {general_name}"
        glisten_choice = choice(GLISTENS_VERB)
    return " ".join([
        f"The {listify_words(item.parts)}",
        f"are all covered in {choice(CARVINGS_ADJECTIVE)}",
        f"{choice(CARVINGS_NOUN)}, and the",
        f"{second_sentence} {glisten_choice}",
        f"with {a_an(choice(GLISTENS_ADJECTIVE))} {choice(GLISTENS_NOUN)}."
    ])


def common_details(item):
    details = shuffled(DETAIL_NOUN[item.rarity])
    pops = shuffled([0, 1, 2])
    in_by = choice(["in", "with", "by"])
    return " ".join([
        f"The {is_are(item.parts[pops.pop()])}",
        f"{ADJECTIVES.pop()} and {ADJECTIVES.pop()}, and the",
        f"{is_are(item.parts[pops.pop()])}",
        f"covered {in_by} {details.pop()} and {details.pop()}."
    ])


def get_details(item):
    return {
        "rare": _choose([patinas_etchings, inlays], [10, 1]),
        "legendary": _choose([patinas_etchings, inlays], [5, 1]),
        "mythical": _choose([patinas_etchings, inlays], [5, 2])
    }.get(item.rarity, common_details)(item)


def get_make():
    return choice([
        "shaped",
        "formed",
        "fashioned",
        "made",
        "constructed",
        "assembled"
    ])


#————————————————————————————————— item name —————————————————————————————————#


def item_name(item):
    new_name = []

    if item.base_name in ["hood", "coif"]:
        new_name.extend(common_name(item))

    else:
        new_name.extend({
            "rare": rare_name,
            "legendary": legendary_name,
            "mythical": mythical_name
        }.get(item.rarity, common_name)(item))

    return " ".join(new_name)


def rare_name(item):
    return choice([
        [choice(ADJECTIVES), item.material, item.base_name],
        [choice(CONDITION[item.rarity]), item.material,
         item.base_name, choice(ABSTRACT)]
    ])


def legendary_name(item):
    return choice([
        [choice(ADJECTIVES), item.base_name, choice(ABSTRACT)],
        [choice(ADJECTIVES), item.material, item.base_name, choice(ABSTRACT)],
        [choice(ADJECTIVES), choice(NOUNS), choice(ABSTRACT)],
        [choice(ADJECTIVES), item.material, choice(NOUNS)],
        [choice(ADJECTIVES), choice(NOUNS), "of " + item.material],
        [choice(ADJECTIVES), item.material, choice(NOUNS), choice(ABSTRACT)]
    ])


def mythical_name(item):
    return choice([
        [choice(PREFIXES), choice(VERBS)],
        [choice(PREFIXES)+"'s", choice(NOUNS)],
        [choice(PREFIXES)+"'s", choice(ADJECTIVES), choice(NOUNS)],
        [choice(ADJECTIVES), choice(NOUNS), choice(ABSTRACT)]
    ])


def common_name(item):
    if item.material not in ["hide", "leather"]:
        return choice([
            [item.rarity, item.material, item.base_name],
            [choice(CONDITION[item.rarity]), item.material, item.base_name]
        ])
    return choice([
        [item.rarity, item.material, item.base_name],
        [choice(SOFT_ADJECTIVE[item.rarity]), item.material, item.base_name]
    ])


#————————————————————————————————— item stats ————————————————————————————————#


def item_stats(item):
    return {
        "weapon": weapon_stats,
        "armor": armor_stats
    }[item.item_class](item)


def weapon_stats(item):
    stats = WEAPON_STAT_DATA[item.sub_type][item.base_type][item.rarity]
    stats = [round(variance(x), ndigits=2) for x in stats]

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
    combs = [round(wt*variance(x*y), ndigits=2) for x, y in zip(stats, mults)]

    return {
        "protection": combs[0],
        "movement": combs[1],
        "noise": combs[2],
        "luck": combs[3]
    }


#——————————————————————————————————— data ————————————————————————————————————#
WEAPON_MATERIAL = [
    "iron",
    "steel",
    "bone",
    "obsidian",
    "electrum",
    "adamantite",
    "meteorite",
]


LIGHT_ARMOR_MATERIAL = [
    "hide",
    "leather",
    "obsidian",
    "electrum",
    "bone",
    "adamantite",
    "meteorite"
]


HEAVY_ARMOR_MATERIAL = [
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


ARMOR_CONSTRUCTION = {
    "ArmorLight": [
        "lamellar",
        "scale"
    ],
    "ArmorHeavy": [
        "laminar",
        "plate"
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


#———————————————————————————————— decorations ————————————————————————————————#


INLAYS = [
    "gold",
    "silver",
    "onyx",
    "obsidian",
    "amethyst",
    "emerald",
    "ruby",
    "jade",
    "turquoise",
    "zircon",
    "howlite",
    "bloodstone",
    "topaz",
    "sardonyx",
    "gypsum",
    "opal",
    "coral",
    "moonstone",
    "sapphire",
    "spessartine",
    "charoite",
    "copper",
    "pearl"
]


GLISTENS_VERB = [
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


GLISTENS_ADJECTIVE = [
    "rainbow",
    "verdigris",
    "prismatic",
    "opalescent",
    "nacreous",
    "variegated",
    "iridescent"
]


GLISTENS_NOUN = [
    "patina",
    "shimmer",
    "shine",
    "sheen",
    "brilliance",
    "luster",
    "finish",
]


CARVINGS_ADJECTIVE = [
    "intricate",
    "elaborate",
    "detailed",
    "elegant",
    "sophisticated",
    "complex",
    "labyrinthine",
    "minute",
]


CARVINGS_NOUN = [
    "carvings",
    "etchings",
    "patterns",
    "inscriptions",
    "engravings"
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
    "uncommon": [
        "burnished",
        "fine",
        "satin"
    ],
    "rare": [
        "fine",
        "satin",
        "engraved"
    ],
    "legendary": [
        "fine",
        "satin",
        "engraved"
    ],
    "mythical": [
        "fine",
        "satin",
        "engraved"
    ]
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


#——————————————————————————————————— names ———————————————————————————————————#


ABSTRACT = [
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
]


ADJECTIVES = [
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
]


PREFIXES = [
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
]


VERBS = [
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
]


NOUNS = [
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
