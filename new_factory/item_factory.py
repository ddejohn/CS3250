import factory_util as util


class Item:
    pass


class ItemBuilder:
    @staticmethod
    def forge():
        new_item = util.NewItem()
        item_data = {
            "item_class": new_item.item_class,
            "base_type": new_item.base_type,
            "sub_type": new_item.sub_type,
            "rarity": new_item.rarity,
            "name": new_item.name,
            "description": new_item.description,
            "stats": new_item.stats
        }

        forged_item = Item()
        for key, val in item_data.items():
            setattr(forged_item, key, val)
        return forged_item


if __name__ == "__main__":
    for _ in range(100):
        item = ItemBuilder.forge()
        print(util.verbose_print(vars(item)))
