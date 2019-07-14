from random import shuffle
from random import choice
from operator import add
import matplotlib.pyplot as plt

class Maze:
    """Generate a maze with 'rooms' on intersections, corners, and dead-ends.
    """

    moves = [
        [(0, 2), (0, 1)], [(0, -2), (0, -1)],
        [(-2, 0), (-1, 0)], [(2, 0), (1, 0)]
    ]

    rules = [
        [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0],
        [1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1],
        [1, 1, 1, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0],
        [0, 1, 0, 1]
    ]

    def __init__(self):
        self.rebuild()

    def __call__(self, *args):
        x, y, *val = args
        if val:
            self.maze[y][x] = val.pop()
        return self.maze[y][x]

    def rebuild(self):
        """Generate a new maze
        """
        x = choice([10, 12, 14, 18])
        y = 148//x
        rng_x = range(1, x+1, 2)
        rng_y = range(1, y+1, 2)

        self.maze = [[0 for i in range(x+1)] for j in range(y+1)]
        self.grid = [(i, j) for i in rng_x for j in rng_y]
        self.path = [choice(self.grid)]
        self.rooms = []
        self._generate()

    def reroom(self, obj):
        """Reassign maze rooms as obj
        """
        for room in self.rooms:
            self(*room, obj)

    def draw(self):
        """Show an image of the generated maze
        """
        _, axes = plt.subplots(figsize=(10, 10))
        axes.set_aspect(1.0)
        plt.xticks([])
        plt.yticks([])
        plt.pcolormesh(self.maze, cmap=plt.cm.get_cmap("tab20b"))
        plt.show()

    def _generate(self):
        k = self.path[0]
        self.grid.remove(k)
        while self.grid:
            n = len(self.path)
            nsew = self._prb_lnk(k)
            shuffle(nsew)
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
        self._get_rooms()

    def _get_rooms(self):
        for coord in self.path:
            if self._neighbors(coord) in self.rules:
                self.rooms.append(coord)
                self(*coord, 2)
        self(*self.path[0], 2)
        self(*self.path[-2], 2)

    def _prb_lnk(self, coord):
        nsew = []
        for move in self.moves:
            prb = tuple(map(add, move[0], coord))
            lnk = tuple(map(add, move[1], coord))
            nsew.append([prb, lnk])
        return nsew

    def _neighbors(self, coord):
        i, j = coord
        return [self(i-1, j), self(i+1, j), self(i, j-1), self(i, j+1)]

    def _walk(self, coords):
        prb, lnk = coords
        self(*prb, 1)
        self(*lnk, 1)
