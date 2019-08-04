from random import choice

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
