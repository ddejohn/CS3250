from random import choice, choices
import factory_util as util


class Item:
    pass


class ItemBuilder:
    def __init__(self):
        self.item_class,\
            self.base_type,\
            self.sub_type,\
            self.item_type = util.new_item()
        self.base_name = util.base_name(self)
        self.rarity,\
            self.material_weights = util.item_rarity()
        self.material = util.item_material(self)
        self.parts = util.item_parts(self)
        self.secondary = util.get_secondary(self)
        self.forge()

    def forge(self):
        item_data = {
            "item_class": self.item_class,
            "base_type": self.base_type,
            "sub_type": self.sub_type,
            "name": util.item_name(self),
            "description": util.item_description(self),
            "stats": util.item_stats(self)
        }

        new_item = Item()
        for key, val in item_data.items():
            setattr(new_item, key, val)
        return new_item
