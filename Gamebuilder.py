"""Dork type factories"""

from copy import deepcopy
from random import choices, choice, randint
from operator import add
from numpy import full as npf
import matplotlib.pyplot as plt
import factory_data
import yaml


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

    @classmethod
    def build(cls, weights=None):

        weights = {
            "player": [8, 0, 0, 7, 5, 10]
        }.get(weights, [8, 35, 3, 7, 5, 10])

        item_type = choice(choices(
            population=list(cls.types.keys()),
            weights=weights,
            k=len(list(cls.types.keys()))
        ))

        item_name = choice(choices(
            population=cls.types[item_type],
            k=len(cls.types[item_type])
        ))

        return cls._forge(item_name, item_type)

    @classmethod
    def _generate(cls, unique_type, stats, item_name, item_type):
        return {
            "name": item_name,
            "type": item_type,
            "description": unique_type,
            "stats": stats
        }

    @classmethod
    def _stats(cls, unique_type, item_name, item_type):
        stats = factory_data.stats(item_type.split()[0])
        return cls._generate(unique_type, stats, item_name, item_type)

    @classmethod
    def _forge(cls, item_name, item_type):
        new_name = []
        unique_type = ""
        build = cls.sequence[item_type]

        seq = choice(choices(
            population=build["seq"],
            weights=build["w"],
            k=len(build["seq"])
        ))

        for lists in seq:
            if isinstance(lists, dict):
                this_list = lists.get(
                    item_type, lists.get("usable", ['']))
            elif lists:
                this_list = lists
            else:
                this_list = ['']

            this_word = choice(choices(
                population=this_list,
                k=len(this_list)
            ))

            if this_word:
                if this_word in cls.suffixes:
                    new_name[-1] += this_word
                    unique_type = item_name
                    item_type = "legendary"
                else:
                    new_name.append(this_word)
            else:
                new_name.append(item_name)

        item_name = " ".join(new_name)
        return cls._stats(unique_type, item_name, item_type)


class PlayerFactory:
    """Generate players for a room"""

    @staticmethod
    def build(i, room):
        """Make a player, give them items"""

        new_player = {
            "name": f"player {i}",
            "description": f"player {i} description",
            "locataion": room,
            "inventory": {},
            "equipped": {}
        }

        for _ in range(randint(1, 3)):
            new_item = ItemFactory.build("player")
            new_player["inventory"][new_item["name"]] = new_item

        for key, val in new_player["inventory"].items():
            new_player["equipped"][key] = val

        return new_player


class RoomFactory:
    """Generate rooms for a given maze"""

    moves = {
        "north": (0, 1), "south": (0, -1),
        "east": (1, 0), "west": (-1, 0),
    }

    @classmethod
    def build(cls, maze, rooms):
        cls.maze = maze
        cls.rooms = rooms
        cls.worldmap = {}
        return cls._make_rooms()

    @classmethod
    def _make_rooms(cls):
        i = 0
        for room in cls.rooms:
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
                new_item = ItemFactory.build()
                new_room["inventory"][new_item["name"]] = new_item

            for _ in range(randint(0, 2)):
                new_player = PlayerFactory.build(i, new_room)
                new_room["players"][new_player["name"]] = new_player

            cls.worldmap[room] = new_room
            i += 1

        return cls._get_adj()

    @classmethod
    def _get_adj(cls):
        for coord, room in cls.worldmap.items():
            for direction in cls.moves:
                searching = True
                position = coord
                while searching:
                    position = tuple(map(add, position, cls.moves[direction]))
                    if cls.maze[position] == -2:
                        room["adjacent"][direction] = None
                        searching = False
                    elif cls.maze[position] == 1:
                        room["adjacent"][direction] = cls.worldmap[position]["name"]
                        searching = False

        for coord, room in deepcopy(cls.worldmap).items():
            cls.worldmap[room.pop("name")] = cls.worldmap.pop(coord)

        return cls.worldmap


class MazeFactory:
    """Generate a maze with rooms on intersections, corners, and dead-ends"""

    moves = factory_data.MOVES
    wall_color, path_color, room_color, player_color = (-2, 0, 1, 2)
    rules = factory_data.rules(wall_color, path_color)

    @staticmethod
    def draw(maze):
        plt.figure(figsize=(len(maze[0])//2, len(maze)//2))
        plt.pcolormesh(maze, cmap=plt.cm.get_cmap("tab20b"))
        plt.axis("equal")
        plt.axis("off")
        plt.ion()
        plt.show()

    @staticmethod
    def update(maze):
        plt.pcolormesh(maze, cmap=plt.cm.get_cmap("tab20b"))
        plt.axis("equal")
        plt.axis("off")
        plt.draw()

    @classmethod
    def build(cls):
        x = choice([10, 12, 14, 18])
        y = 148//x

        cls.rng_x = range(1, x+1, 2)
        cls.rng_y = range(1, y+1, 2)

        cls.maze = npf((x+1, y+1), cls.wall_color)
        cls.grid = [(i, j) for i in cls.rng_x for j in cls.rng_y]
        cls.path = [choice(cls.grid)]
        cls.rooms = []

        return cls._generate()

    @classmethod
    def _generate(cls):
        k = cls.path[0]
        cls.grid.remove(k)
        while cls.grid:
            n = len(cls.path)
            nsew = cls._prb_lnk(k)
            for prb_lnk in nsew:
                probe, _ = prb_lnk
                if probe in cls.grid:
                    cls._walk(prb_lnk)
                    cls.grid.remove(probe)
                    cls.path.extend(prb_lnk)
                    break
            if n == len(cls.path):
                k = cls.path[max(cls.path.index(k)-1, 1)]
            else:
                k = cls.path[-1]
        return cls._get_rooms()

    @classmethod
    def _get_rooms(cls):
        for coord in cls.path:
            neighbors = cls._neighbors(coord)
            if neighbors in cls.rules:
                cls.rooms.append(coord)
                cls.maze[coord] = cls.room_color
        cls.maze[cls.path[0]] = cls.room_color
        cls.maze[cls.path[-2]] = cls.player_color

        return {
            "maze": cls.maze.tolist(),
            "rooms": RoomFactory.build(cls.maze, cls.rooms),
        }

    @classmethod
    def _prb_lnk(cls, coord):
        nsew = []
        for move in cls.moves:
            prb = tuple(map(add, move[0], coord))
            lnk = tuple(map(add, move[1], coord))
            nsew.append([prb, lnk])
        return choices(nsew, k=len(nsew))

    @classmethod
    def _neighbors(cls, coord):
        i, j = coord
        return [
            cls.maze[(i-1, j)],
            cls.maze[(i+1, j)],
            cls.maze[(i, j-1)],
            cls.maze[(i, j+1)],
        ]

    @classmethod
    def _walk(cls, coord):
        prb, lnk = coord
        cls.maze[prb] = cls.path_color
        cls.maze[lnk] = cls.path_color


def write(data):   
    data = {
        "maze": data["maze"],
        "rooms": data["rooms"]
    }

    file_name = "./factory_output.yml"
    with open(file_name, "w") as save_file:
        yaml.safe_dump(
            data,
            save_file, indent=4, width=80,
            default_flow_style=False
        )