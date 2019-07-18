from copy import deepcopy
from random import choices, choice, randint
from operator import add
from numpy import full as npf
import matplotlib.pyplot as plt
import factory_data


class MazeFactory:
    """Generate a maze with rooms on intersections, corners, and dead-ends"""

    RoomFactory()
    PlayerFactory()
    ItemFactory()

    moves = factory_data.MOVES
    wall_color, path_color, room_color, player_color = (-2, 0, 1, 2)
    rules = factory_data.rules(wall_color, path_color)

    def __init__(self):
        x = choice([10, 12, 14, 18])
        y = 148//x

        self.rng_x = range(1, x+1, 2)
        self.rng_y = range(1, y+1, 2)

        self.maze = npf((x+1, y+1), self.wall_color)
        self.grid = [(i, j) for i in self.rng_x for j in self.rng_y]
        self.path = [choice(self.grid)]
        self.x_draw = len(self.maze[0])//2
        self.y_draw = len(self.maze)//2
        self.rooms = []

    def __call__(self):
        return self._generate()

    def _generate(self):
        k = self.path[0]
        self.grid.remove(k)
        while self.grid:
            n = len(self.path)
            nsew = self._prb_lnk(k)
            for prb_lnk in nsew:
                probe, _ = prb_lnk
                if probe in self.grid:
                    self._walk(prb_lnk)
                    self.grid.remove(probe)
                    self.path.extend(prb_lnk)
                    break
            if n == len(self.path):
                k = self.path[max(self.path.index(k)-1, 1)]
            else:
                k = self.path[-1]
        return self._get_rooms()

    def _get_rooms(self):
        for coord in self.path:
            neighbors = self._neighbors(coord)
            if neighbors in self.rules:
                self.rooms.append(coord)
                self.maze[coord] = self.room_color
        self.maze[self.path[0]] = self.room_color
        self.maze[self.path[-2]] = self.player_color

        return {
            "maze": self.maze.tolist(),
            "rooms": RoomFactory(self.maze, self.rooms)(),
        }

    def _prb_lnk(self, coord):
        nsew = []
        for move in self.moves:
            prb = tuple(map(add, move[0], coord))
            lnk = tuple(map(add, move[1], coord))
            nsew.append([prb, lnk])
        return choices(nsew, k=len(nsew))

    def _neighbors(self, coord):
        i, j = coord
        return [
            self.maze[(i-1, j)],
            self.maze[(i+1, j)],
            self.maze[(i, j-1)],
            self.maze[(i, j+1)],
        ]

    def _walk(self, coord):
        prb, lnk = coord
        self.maze[prb] = self.path_color
        self.maze[lnk] = self.path_color

    def _draw(self):
        plt.figure(figsize=(self.x_draw, self.y_draw))
        plt.pcolormesh(self.maze, cmap=plt.cm.get_cmap("tab20b"))
        plt.axis("equal")
        plt.axis("off")
        plt.ion()
        plt.show()

    def _update(self):
        plt.pcolormesh(self.maze, cmap=plt.cm.get_cmap("tab20b"))
        plt.axis("equal")
        plt.axis("off")
        plt.draw()


class RoomFactory:
    """Generate rooms for a given maze"""

    def __init__(self, maze, rooms):
        self.moves = {
            "north": (0, 1), "south": (0, -1),
            "east": (1, 0), "west": (-1, 0),
        }
        self.maze = maze
        self.rooms = rooms
        self.worldmap = {}

    def __call__(self):
        return self._make_rooms()

    def _make_rooms(self):
        i = 0
        for room in self.rooms:
            x, y = room
            new_room = {
                "name": f"room {i}",
                "description": f"room {i} description",
                "x": x,
                "y": y,
                "adjacent": {},
                "players": {},
                "inventory": {},
            }

            for _ in range(randint(1, 7)):
                new_item = ItemFactory()
                new_room["inventory"][new_item["name"]] = new_item

            for _ in range(randint(0, 2)):
                new_player = PlayerFactory(i, new_room)
                new_room["players"][new_player["name"]] = new_player

            self.worldmap[room] = new_room
            i += 1

        return _get_adj(self)

    def _get_adj(self):
        for coord, room in self.worldmap.items():
            for direction in self.moves:
                searching = True
                position = coord
                while searching:
                    position = tuple(map(add, position, self.moves[direction]))
                    if self.maze[position] == 0:
                        room["adjacent"][direction] = None
                        searching = False
                    elif self.maze[position] == 2:
                        room["adjacent"][direction] = self.worldmap[position]["name"]
                        searching = False

        for coord, room in deepcopy(self.worldmap).items():
            self.worldmap[room.pop("name")] = self.worldmap.pop(coord)

        return worldmap


class ItemFactory:
    """Generates a random named item with randomized stats"""
    
    items = factory_data.ITEMS
    names = factory_data.NAMES
    sequence = factory_data.SEQUENCE

    types = items["types"]
    condition = items["condition"]
    material = items["material"]

    posessive = names["posessive"]
    nonposessive = names["nonposessive"]
    suffixes = names["suffixes"]
    abstract = names["abstract"]
    adjectives = names["adjectives"]

    def __init__(self):
        self.item_name = str
        self.item_type = str

    def __call__(self, weights=None):
        weights = {
            "player": [8, 0, 0, 7, 5, 10]
        }.get(weights, [8, 35, 3, 7, 5, 10])

        self.item_type = choice(choices(
            population=list(self.types.keys()),
            weights=weights,
            k=len(list(self.types.keys()))
        ))

        self.item_name = choice(choices(
            population=self.types[self.item_type],
            k=len(self.types[self.item_type])
        ))

        return self.forge()

    def _generate(self, unique_type, stats):
        return {
            "name": self.item_name,
            "type": self.item_type,
            "description": unique_type,
            "stats": stats
        }

    def _stats(self, unique_type):
        stats = factory_data.stats(self.item_type.split()[0])
        return self.generate(unique_type, stats)

    def _forge(self):
        new_name = []
        unique_type = ""
        build = self.sequence[self.item_type]

        seq = choice(choices(
            population=build["seq"],
            weights=build["w"],
            k=len(build["seq"])
        ))

        for lists in seq:
            if isinstance(lists, dict):
                this_list = lists.get(
                    self.item_type, lists.get("usable", ['']))
            elif lists:
                this_list = lists
            else:
                this_list = ['']

            this_word = choice(choices(
                population=this_list,
                k=len(this_list)
            ))

            if this_word:
                if this_word in self.suffixes:
                    new_name[-1] += this_word
                    unique_type = self.item_name
                    self.item_type = "legendary"
                else:
                    new_name.append(this_word)
            else:
                new_name.append(self.item_name)

        self.item_name = " ".join(new_name)
        return self.stats(unique_type)


class PlayerFactory:
    """Generate players for a room"""

    def __init__(self, i, room):
        """Make a player, give them items"""

        new_player = {
            "name": f"player {i}",
            "description": f"player {i} description",
            "locataion": room,
            "inventory": {},
            "equipped": {}
        }

        for _ in range(randint(1, 3)):
            new_item = ItemFactory("player")
            new_player["inventory"][new_item["name"]] = new_item

        for key, val in new_player["inventory"].items():
            new_player["equipped"][key] = val

        return new_player
