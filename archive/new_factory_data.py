from random import randint


TYPES = [
    "weapon",
    "armor",
    "jewelry",
    "magic",
    "potion",
]


ITEMS = {
    "weapon": {
        "big": [
            "longsword",
            "claymore,"
            "staff",
            "longbow",
            "recurve bow",
            "bardiche",
            "meteor hammer",
            "war hammer",
            "halberd",
            "spear",
            "battle axe",
            "glaive",
            "scythe",
        ],
        "small": [
            "bladed caestus",
            "barbed caestus",
            "cutlass",
            "falchion",
            "harpe"
            "sabre",
            "scimitar",
            "backsword",
            "sickle",
            "dagger",
            "falcata"
            "mace",
            "morning star",
            "club",
            "blade",
            "shortsword",
        ]
    },
    "armor": {
        "body": [
            "brigandine",
            "cuirass",
            "vest",
            "hauberk",
            "coif",
            "gamebeson",
        ],
        "limbs": [
            "helm",
            "gorget",
            "morion",
            "hood",
            "vambrace",
            "gauntlets",
            "gloves",
            "boots",
            "sabatons",
        ]
    },
    "jewelry": [
        "ring",
        "amulet",
        "circlet",
        "talisman",
        "pendant",
        "necklace",
        "torc",
    ],
    "magic": [
        "shard",
        "tome",
        "scroll"
        "dust",
        "orb",
        "soulgem"
        "magestone",
        "horn",
    ],
    "potion": [
        "potion",
        "philter",
        "draught",
        "infusion",
        "elixir",
        "tincture",
    ]
}


RARITY = {
    "weapon": [
        "crude",
        "common",
        "uncommon",
        "rare",
        "mythical",
    ],
    "armor": [
        "crude",
        "common",
        "uncommon",
        "rare",
        "legendary",
    ],
    "jewelry": [
        "crude",
        "flawed",
        "fair",
        "fine",
        "pristine"
    ],
    "magic": [
        "petty",
        "lesser",
        "common",
        "greater",
        "grand"
    ],
    "potion": [
        "wretched",
        "spoiled",
        "adequate",
        "fine",
        "pure"
    ]
}


MATERIAL = {
    "weapon": [
        "bone",
        "iron",
        "steel",
        "glass",
        "golden",
        "silver",
        "bronze",
        "meteorite",
        "adamantine"
    ],
    "armor": [
        "bone",
        "dragonscale",
        "hide",
        "iron",
        "steel",
        "leather",
        "plate",
        "mail"
    ],
    "jewelry": [
        "bone",
        "gold",
        "silver",
        "onyx",
        "obsidian",
        "amethyst",
        "emerald",
        "ruby",
        "jade",
        "turquoise",
        "ivory",
        "bronze",
        "copper",
        "meteorite",
        "adamantine"
    ],
    "magic": [
        "bone",
        "gold",
        "silver",
        "onyx",
        "obsidian",
        "amethyst",
        "emerald",
        "ruby",
        "jade",
        "turquoise",
        "ivory",
        "bronze",
        "copper",
        "meteorite",
        "adamantine"
    ],
    "potion": {
        1: [
            "goat's",
            "wolf's",
            "troll's",
            "bear's",
            "ghost's",
            "dragon's",
            "faerie's",
            "werewolf's",
            "centaur's",
            "giant's",
            "nymph's",
            "dragon's",
            "goblin's",
        ],
        2: [
            "hair",
            "eye",
            "fang",
            "claw",
            "feather",
            "blood",
            "bone",
            "marrow",
            "teeth",
        ],
    }
}


NAMES = {
    "abstract": [
        "of blooding",
        "of humiliation",
        "of hubris",
        "of the hunt",
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
        "of the heretic",
        "of the prophet",
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
        "of the night",
        "of the stars",
        "of the dawn",
        "of the dusk",
        "of the morning",
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
        "of ruining",
        "of fury",
        "of disgust",
        "of friendship",
        "of calming",
        "of shame",
        "of pity",
        "of envy",
        "of suffering",
        "of weeping",
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
        "of exsanguination"
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
    "nonposessive": [
        "doom",
        "death",
        "hate",
        "fear",
        "soul",
        "sky",
        "mind",
        "god",
        "star",
        "shadow"
        "sun",
        "moon",
        "storm"
    ],
    "posessive": [
        "wolf",
        "troll",
        "goliath",
        "raven",
        "dragon",
        "crow",
        "widow",
        "wraith",
        "heart"
    ],
    "suffixes": [
        "sbane",
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
        "corrupter",
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
}