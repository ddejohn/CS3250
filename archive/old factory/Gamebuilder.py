"""Dork type factories"""

from copy import deepcopy
from random import choices, choice, randint, shuffle
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

    @staticmethod
    def build(weights=None):

        weights = {
            "player": [8, 0, 0, 7, 5, 10]
        }.get(weights, [8, 35, 3, 7, 5, 10])

        item_type = choice(choices(
            population=list(ItemFactory.types.keys()),
            weights=weights,
            k=len(list(ItemFactory.types.keys()))
        ))

        item_name = choice(choices(
            population=ItemFactory.types[item_type],
            k=len(ItemFactory.types[item_type])
        ))

        return ItemFactory._forge(item_name, item_type)

    @staticmethod
    def _generate(unique_type, stats, item_name, item_type):
        return {
            "name": item_name,
            "type": item_type,
            "description": unique_type,
            "stats": stats
        }

    @staticmethod
    def _stats(unique_type, item_name, item_type):
        stats = factory_data.stats(item_type.split()[0])
        return ItemFactory._generate(unique_type, stats, item_name, item_type)

    @staticmethod
    def _forge(item_name, item_type):
        new_name = []
        unique_type = ""
        build = ItemFactory.sequence[item_type]

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
                if this_word in ItemFactory.suffixes:
                    new_name[-1] += this_word
                    unique_type = item_name
                    item_type = "legendary"
                else:
                    new_name.append(this_word)
            else:
                new_name.append(item_name)

        item_name = " ".join(new_name)
        return ItemFactory._stats(unique_type, item_name, item_type)


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
        "north": (0, 2), "south": (0, -2),
        "east": (2, 0), "west": (-2, 0),
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
                    position = tuple(
                        sum(x) for x in zip(position, cls.moves[direction])
                    )
                    if position not in cls.rooms or cls.maze[position] == MazeFactory.wall_color:
                        room["adjacent"][direction] = None
                        searching = False
                    elif cls.maze[position] == MazeFactory.room_color:
                        room["adjacent"][direction] = \
                            cls.worldmap[position]["name"]
                        searching = False

        for coord, room in deepcopy(cls.worldmap).items():
            cls.worldmap[room.pop("name")] = cls.worldmap.pop(coord)

        return cls.worldmap


class MazeFactory:
    """Generate a maze with rooms on intersections, corners, and dead-ends"""

    wall_color, path_color, room_color, player_color = (0, 1, -2, 2)
    moves = factory_data.MOVES
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

    @staticmethod
    def build():

        x = choice([10, 12, 14, 18])
        y = 148//x

        maze = npf((x+1, y+1), MazeFactory.wall_color)
        grid = [(i, j) for i in range(1, x+1, 2) for j in range(1, y+1, 2)]
        path = [choice(grid)]
        rooms = []
        k = path[0]
        grid.remove(k)

        while grid:
            n = len(path)
            nsew = []
            for move in MazeFactory.moves:
                probe = tuple(sum(x) for x in zip(move[0], k))
                link = tuple(sum(x) for x in zip(move[1], k))
                nsew.append([probe, link])
            shuffle(nsew)
            for probe in nsew:
                prb, lnk = probe
                if prb in grid:
                    maze[prb] = MazeFactory.path_color
                    maze[lnk] = MazeFactory.path_color
                    grid.remove(prb)
                    path.extend(probe)
                    break
            if n == len(path):
                k = path[max(path.index(k)-1, 1)]
            else:
                k = path[-1]

        for coord in path:
            i, j = coord
            neighbors = [
                maze[i-1, j],
                maze[i+1, j],
                maze[i, j-1],
                maze[i, j+1]
            ]
            if neighbors in MazeFactory.rules:
                rooms.append(coord)
                maze[coord] = MazeFactory.room_color

        return {
            "maze": maze.tolist(),
            "rooms": RoomFactory.build(maze, rooms)
        }
