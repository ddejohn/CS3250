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
    adjacency list (N, S, E, W, NE, NW, SE, SW, up, down) as a dict, maybe?
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

### 6/3/19 class notes

**TODO:**
* read scrum guide
* ~~get books~~
* VENV
* ***5 dysfunctions, design patterns (FOR FIRST TEST)***

### Zork notes

Bit of a learning curve. Not sure if there's a `help` function of any sort, but that sort of added to the appeal for me personally.


**Things I like:**
* The simplicity—seriously, this game is charming as heck
* The writing is short and sweet—some of the descriptions are a little bland, but in general I've really enjoyed it
* There's a definite rush of excitement when you uncover a clue

**Things I don't like:**
* Some commands don't seem to have enough aliases
* Sometimes movement seems unable to be reversed (i.e., go east, then go west, sometimes you end up somewhere other than where you previously were)

### 6/6/19 class notes

**TODO:**
* ~~VENV, unit tests~~
* read *The Cathedral and the Bazaar*

### Graph theory research notes

Mostly review for me, although the video I watched contained some interesting worked examples:

* The lecturer introduces the results of two studies considering the relati ve promiscuity between men and women with opposite gender partners. Both results are mathematically proven erroneous using only basic graph theory properties.
* The Graph Coloring Problem is discussed in the context of final exam scheduling for classes with overlapping enrollment.

Sources: [Lec 6 | MIT 6.042J Mathematics for Computer Science, Fall 2010](https://youtu.be/h9wxtqoa1jY)

### 6/6/19 class notes


* Program requirements
- statements that define and quantify what the program needs to do
- the work requirements aren't used in the same way as elsewhere
- software requirements tend to be negotiable

* Functional requirements
- what a program *needs* to do
- binary; yes or no

* Non-functional requirements
- the manner in which the functional requirements need to be achieved
- performance, usability, maintainability
- tend to be on scale

* Design constraints
- statements that constrain the ways in which the software can be designed and implemented
- platform, language, database, webapp, GUI, etc.