def _equip_item(self, item=None):
    inv = self.items
    if not item:
        out = "You equipped nothing. Good job, idiot."
    elif item in inv.keys() and inv[item].equipable:
        if not inv[item].equipped:
            self._equipped.append(item)
            inv[item].equipped = True
            out = f"You have equipped {item}.\n  {inv[item].description}"
        else:
            out = f"{item} is already equipped, you dunce."
    else:
        if item not in inv.keys():
            out = f"You don't even have one of those!"
        elif not inv[item].equipable:
            out = f"You can't equip that, silly goose."
    return out

def _unequip_item(self, item=None):
    inv = self.items
    if not item:
        out = "Gotta be a little bit more specific than that, bud."
    elif item in inv.keys() and inv[item].equipped:
        self._equipped.remove(item)
        inv[item].equipped = False
        out = f"You put {item} away."
    else:
        if item not in inv.keys():
            out = f"You don't even have one of those!"
        elif not inv[item].equipped:
            out = f"You don't have {item} equipped, you walnut."
    return out

def _add_item(self, item=None):
    items = self._location.items
    inv = self.items
    if (items and not item):
        for k in items.keys() & inv.keys():
            for stat in inv[k].stats.keys() & items[k].stats.keys():
                print(f"You gained {items[k].stats[stat]} {k}")
                inv[k].stats[stat] += items[k].stats[stat]
            items.pop(k)
        for k in items.keys() - inv.keys():
            inv[k] = items.pop(k)
            print(f"You picked up {inv[k].name}")
        out = ""

    elif (items and item) and (item in items):
        if item in items.keys() & inv.keys():
            for stat in inv[item].stats:
                out = f"You gained {items[item].stats[stat]} {item}"
                inv[item].stats[stat] += items.pop(item).stats[stat]
        elif item in items.keys() - inv.keys():
            inv[item] = items.pop(item)
            out = f"You picked up {inv[item].name}"

    elif (items and item) and (item not in items):
        out = f"There is no {item} here."
    elif not items and item:
        out = "Are you high?"
    else:
        out = "You tried to pick nothing up. You succeeded."
    return out
