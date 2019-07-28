import new_factory_data


_TYPES = new_factory_data.TYPES
_ITEMS = new_factory_data.ITEMS
_RARITY = new_factory_data.RARITY
_MATERIAL = new_factory_data.MATERIAL
_NAMES = new_factory_data.NAMES


class Stats:
    """stats for items"""

    def __init__(self):
        self.attack = int
        self.strength = int
        self.weight = int
        self.luck = int
        self.equipable = bool


class Item(Stats):
    """An obtainable/usable item"""

    def __init__(self):
        super().__init__()
        self.name = str
        self.description = str
        self.type = str


class ItemData:
    def __init__(self):
        self.type = str
        self.size = str
        self.rarity = str
        self.material = str
        self.condition = str


class ItemFactory:
    """randomly generate a useful item"""

    def __call__():
        return type_picker(ItemData())

    def type_picker(item_data: ItemData) -> ItemFactory.rarity_picker:
        # pick weighted random item type
        # if armor or weapon, pick size
        return ItemFactory.rarity_picker(item_data)

    def rarity_picker(item_data: ItemData) -> ItemFactory.material_picker:
        # weighted random item rarity
        return ItemFactory.material_picker(item_data)

    def material_picker(item_data: ItemData) -> ItemFactory.condition_picker:
        # by rarity
        return ItemFactory.condition_picker(item_data)

    def condition_picker(item_data: ItemData) -> ItemFactory.forge:
        # by rarity, material
        return ItemFactory.forge(item_data)

    def forge(item_data: ItemData):
        make_this = {
            "weapon": weapon_builder,
            "armor": armor_builder,
            "magic": magic_builder,
            "potion": potion_builder,
            "jewelry": jewelry_builder,
        }[item_data.type]

        return make_this(item_data)

    def weapon_builder(item_data: ItemData) -> Item:
        # size
        # base name
        # rarity
        # material
        # condition
        pass

    def armor_builder(item_data: ItemData) -> Item:
        pass

    def magic_builder(item_data: ItemData) -> Item:
        pass

    def potion_builder(item_data: ItemData) -> Item:
        pass

    def jewelry_builder(item_data: ItemData) -> Item:
        pass



# def BuilderClass(X):
#     class BuilderType(X):
#         def __init__(self):
#             super().__init__()
#     return BuilderType
