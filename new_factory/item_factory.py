import factory_util as util


class Item:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


class ItemBase:
    def __init__(self):
        super().__init__()
        self.item_class,\
            self.base_type,\
            self.sub_type,\
            self.item_type = util.build_item()
        self.rarity,\
            self.material_weights = util.item_rarity()


class ItemConstruction:
    def __init__(self):
        super().__init__()
        self.base_name = util.base_name(self)
        self.material = util.item_material(self)
        self.parts = util.item_parts(self)
        self.secondary = util.item_secondary(self)


class NewItem(ItemConstruction, ItemBase):
    def __init__(self):
        super().__init__()
        self.name = util.item_name(self)
        self.description = util.item_description(self)
        self.stats = util.item_stats(self)


class ItemBuilder:
    @staticmethod
    def forge():
        new_item = NewItem()
        item_data = {
            "item_class": new_item.item_class,
            "base_type": new_item.base_type,
            "sub_type": new_item.sub_type,
            "rarity": new_item.rarity,
            "name": new_item.name,
            "description": new_item.description,
            "stats": new_item.stats
        }

        return Item(**item_data)


if __name__ == "__main__":
    for _ in range(100):
        item = ItemBuilder.forge()
        print(util._verbose_print(vars(item)))
