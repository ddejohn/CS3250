# CS-3250 Notes

### 5/29/19 first thoughts on classes

Classes:


```
Player class
    name
    currrent position as instance of Place
    health/damage
    inventory
        equipped?
    abilities/traits/perks (?)

Place class
    name
    description
    triggers - a method that modifies description field (adds clues as they are discovered)
    items/objects/clues
    enemies/NPCs as instances of Player
    loot (separate from items/objects?)
    adjacency list `(N, S, E, W, NE, NW, SE, SW, up, down)` as a `dict`, maybe?
    transitions allowed (are some directions blocked by clues yet to be discovered? Locked doors?)
```


> Perhaps the adjacency list can be a dict with direction names as keys, and tuples consisting of `(Place, bool)` for an instance of place (or `null`), and a `boolean` to tell us if we can enter. Something like:
>
>
> `{"N", (placeToNorth, true), "S", (placeToSouth, false), "E", (null, false), ...}`


Gameplay loop:


> methods for actions like movement, equipping, inspecting, using... etc.


**Movement:**
* `get` movement command (e.g.: "N" entered into CLI)
* `get` player's current position
* `get` current position's adjacency list
* `set` player's current position to `currentPlace.adj("N")` (or whatever) if able, error if not

**Equipping:**
* `get` equip command (e.g.: "equip knife" entered into CLI)
* `get` player's inventory
* `get` player's equipped (equip multiple? Lantern + knife? Do we need to break Item classes into utilities and weapons)
* `set` player's equipped to `inventory.Items("knife")` if applicable