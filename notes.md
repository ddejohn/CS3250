# CS-3250 Notes
### Devon DeJohn Summer 2019

* Player class
    name
    currrent position as instance of **Place**
    health/damage
    inventory
        equipped?
    abilities/traits/perks (?)

* Place class
    name
    description
    triggers - a method that modifies description field (adds clues as they are discovered)
    items/objects/clues
    enemies/NPCs as instances of **Player**
    loot (separate from items/objects?)
    adjacency list `(N, S, E, W, NE, NW, SE, SW, up, down)` as a `dict`, maybe?
        do we need to distinguish between entrances and exits (trap doors; can only fall through?)
    transitions allowed (are some directions blocked by clues yet to be discovered? Locked doors?)
    
perhaps the adjacency list can be a dict with direction names as keys, and tuples consisting of (Place, bool) for an instance of place (or null), and a boolean to tell us if we can enter. Something like:

    {"N", (placeToNorth, true), "S", (placeToSouth, false), "E", (null, false), "W", (placeToWest, true), ... etc.}

gameplay loop:
    methods for actions like movement, equipping, inspecting, using... etc.
    
* Movement
    [1] get player's movement command (e.g.: "N" entered into CLI)
    [2] get player's current position
    [3] get current position's adjacency list
    [4] change player's current position to Place.adj("N") if able, error if not