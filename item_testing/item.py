"""Create an instance of Item with any number of parents to inherit from"""


class Weapon(object):
    def __init__(self):
        super().__init__()
        self.weapon = "weapon"


class DoorKey(object):
    def __init__(self):
        super().__init__()
        self.doorkey = "door key"


class Potion(object):
    def __init__(self):
        super().__init__()
        self.potion = "potion"


class Item(object):
    def __init__(self):
        super().__init__()


class ItemMaker:
    @staticmethod
    def make(parents):
        if set(parents).issubset({Weapon, Potion, DoorKey}):
            class NewItem(Item, *parents):
                def __init__(self):
                    super().__init__()
            return NewItem()
        return None
