import matplotlib.pyplot as plt
from numpy import zeros as npz
from numpy import where as npw
from random import shuffle
from random import choice
from random import randint
from functools import reduce


def main(size, id_rooms=False):
    # moves = [(0, 2), (0, -2), (-2, 0), (2, 0)]
    # neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # U, D, L, R

    moves = [
        [(0, 2), (0, 1)],
        [(0, -2), (0, -1)],
        [(-2, 0), (-1, 0)],
        [(2, 0), (1, 0)]
    ]

    maze = npz((size+1, size+1), dtype=int)
    el = [(a, b) for a in range(1, size+1, 2) for b in range(1, size+1, 2)]
    rules = [
        [0, 0, 0, 1],  # left end-cap
        [0, 0, 1, 0],  # right end-cap
        [0, 1, 0, 0],  # top end-cap
        [1, 0, 0, 0],  # bottom end-cap
        [1, 1, 1, 0],  # left 3-way
        [1, 1, 0, 1],  # right 3-way
        [1, 0, 1, 1],  # top 3-way
        [0, 1, 1, 1],  # bottom 3-way
        [1, 1, 1, 1],  # 4-way
        [1, 0, 1, 0],  # up-left corner
        [1, 0, 0, 1],  # up-right corner
        [0, 1, 1, 0],  # down-left corner
        [0, 1, 0, 1],  # down-right corner
    ]

    vis = [choice(el)]
    k = vis[0]
    maze[k] = 1
    el.remove(k)

    def get_rooms(m):
        rooms = []
        top_rooms = []
        bottom_rooms = []
        for coord in vis:
            i, j = coord
            udlr = [m[i-1, j], m[i+1, j], m[i, j-1], m[i, j+1]]
            if udlr in rules:
                if id_rooms:
                    m[coord] = 2
                rooms.append(coord)
        for room in rooms:
            if room[0] == 1:
                top_rooms.append(room)
            elif room[0] == m.shape[0]-2:
                bottom_rooms.append(room)
        return m, rooms, top_rooms, bottom_rooms

    def make_soln(m, top_rooms, bottom_rooms):
        dim = m.shape[0]
        while True:
            ct = choice(top_rooms)
            if ct in rooms:
                m[0, ct[1]] = 1
                break
        while True:
            cb = choice(bottom_rooms)
            if cb in rooms:
                m[dim-1, cb[1]] = 1
                break
        return m

    def draw_maze(m):
        fig, ax = plt.subplots(figsize=(10, 10))
        plt.xticks([])
        plt.yticks([])
        ax.pcolormesh(m, cmap=plt.cm.tab20b)
        ax.set_aspect(1.0)
        fig.savefig(
            f"{size}x{size}.png",
            dpi=300,
            bbox_inches="tight",
            pad_inches=0)
        plt.show()

    while len(el) > 0:
        n = len(vis)
        nsew = []
        for i in range(4):
            probe = tuple(sum(x) for x in zip(moves[i][0], k))
            link = tuple(sum(x) for x in zip(moves[i][1], k))
            nsew.append([probe, link])
        shuffle(nsew)
        for a in nsew:
            if a[0] in el:
                probe, link = a
                vis.extend(a)
                maze[probe], maze[link] = 1, 1
                el.remove(probe)
                break
        if n == len(vis):
            k = vis[max(vis.index(k)-1, 1)]
        else:
            k = vis[len(vis)-1]

    maze, rooms, top_rooms, bottom_rooms = get_rooms(maze)
    maze = make_soln(maze, top_rooms, bottom_rooms)
    print(f"{len(rooms)} rooms")
    draw_maze(maze)


if __name__ == "__main__":
    main(10, id_rooms=True)
