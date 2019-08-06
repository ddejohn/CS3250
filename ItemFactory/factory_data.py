from random import choice, sample, randint


RARITY = {
    "crude": [100, 70, 0, 0, 0, 0, 0],
    "common": [40, 100, 50, 10, 0, 0, 0],
    "uncommon": [0, 50, 60, 40, 5, 0, 0],
    "rare": [0, 0, 0, 10, 100, 10, 0],
    "legendary": [0, 0, 0, 0, 30, 100, 10],
    "mythical": [0, 0, 0, 0, 0, 30, 100]
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

ARMOR_MATERIAL = [
    "hide",
    "leather",
    "iron",
    "steel",
    "bone",
    "onyx",
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

BARBS = [
    "fangs",
    "claws",
    "teeth",
    "thorns",
    "spines",
    "spikes",
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
        "gilded",
        "elaborate"
    ],
    "mythical": [
        "ornate",
        "engraved",
        "gilded",
        "elaborate"
    ]
}

DETAIL_NOUN = {
    "crude": [
        "dried blood",
        "dirt",
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
        "ineffable",
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


def ONE_HANDED():
    return {
        "dagger": [
            "fuller",
            "pommel",
            choice(["hilt", "grip"]),
            choice(["cross-guard", "quillon"])
        ],
        "shortsword": [
            "fuller",
            "pommel",
            choice(["hilt", "grip"]),
            choice(["cross-guard", "quillon"])
        ],
        "battle axe": ["pommel", "haft", "hook", "beard"],
        "labrys": ["pommel", "haft", "hook", "beard"]
    }


def TWO_HANDED():
    return {
        "longsword": [
            "fuller",
            "pommel",
            choice(["hilt", "grip"]),
            choice(["cross-guard", "quillon"])
        ],
        "recurve bow": ["nock", "face", "belly", choice(["hilt", "grip"])],
        "scythian bow": ["nock", "face", "belly", choice(["hilt", "grip"])],
        "longbow": ["nock", "face", "belly", choice(["hilt", "grip"])],
        "war hammer": ["face", "cheek", "throat", choice(["haft", "handle"])],
    }


def item_description(item):
    condition = shuffled(CONDITION[item.rarity])
    adjective = shuffled(DETAIL_ADJECTIVE[item.rarity])
    secondary = shuffled(WEAPON_SECONDARY[item.rarity])
    noun = shuffled(DETAIL_NOUN[item.rarity])
    verb = shuffled(DETAIL_VERB[item.rarity])
    parts = shuffled(
        ONE_HANDED().get(item.item_type, TWO_HANDED().get(item.item_type))
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

    if item.rarity in ["crude", "common", "uncommon"]:
        new_name = " ".join([item.rarity, item.material, item.item_type])
    else:
        new_name = item_name(item)

    return {
        "name": new_name,
        "description": f"{first_sentence}\n{last_sentence}"
    }


def item_name(item):
    adjectives = NAMES["adjectives"]
    abstract = NAMES["abstract"]
    prefixes = NAMES["prefixes"]
    verbs = NAMES["verbs"]
    nouns = NAMES["nouns"]
    new_name = []

    if item.rarity == "rare":
        new_name.extend(choice([
            [choice(adjectives), item.material, item.item_type],
            [
                choice(CONDITION[item.rarity]),
                item.material,
                item.item_type,
                choice(abstract)
            ]
        ]))
    elif item.rarity == "legendary":
        new_name.extend(choice([
            [choice(adjectives), item.item_type, choice(abstract)],
            [
                choice(adjectives),
                item.material,
                item.item_type,
                choice(abstract)
            ],
            [choice(adjectives), choice(nouns), choice(abstract)],
            [choice(adjectives), item.material, choice(nouns)],
            [choice(adjectives), choice(nouns), "of "+item.material],
            [choice(adjectives), item.material, choice(nouns), choice(abstract)]
        ]))
    else:
        new_name.extend(choice([
            [choice(prefixes), choice(verbs)],
            [choice(prefixes)+"'s", choice(nouns)],
            [choice(prefixes)+"'s", choice(adjectives), choice(nouns)],
            [choice(adjectives), choice(nouns), choice(abstract)]
        ]))

    return " ".join(new_name)


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
    all_inlays = shuffled(INLAYS)
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
        f"{choice(ETCHINGS)} {choice(CARVINGS)},",
        f"and the {choice(['whole', 'entire'])} {item_type.split()[-1]}",
        f"{choice(GLISTENS)}",
        f"with {a_an(choice(LUSTERS))}",
        f"{choice(PATINAS)}"
    ])
