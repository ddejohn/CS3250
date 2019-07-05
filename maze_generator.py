import matplotlib.pyplot as plt
from numpy import zeros as npz
from numpy import where as npw
from random import shuffle
from random import choice
from random import randint
from functools import reduce


def main(size, id_rooms=False, draw=False):
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

    maze, rooms = _generate_maze(size, id_rooms, draw, moves, rules)
    print(f"{len(rooms)} rooms")
    if draw:
        _draw_maze(maze, size)


def _generate_maze(size, id_rooms, draw, moves, rules):
    m = npz((size+1, size+1), dtype=int)
    el = [(a, b) for a in range(1, size+1, 2) for b in range(1, size+1, 2)]
    vis = [choice(el)]
    k = vis[0]
    el.remove(k)

    while len(el) > 0:
        n = len(vis)
        nsew = []
        for i in range(4):
            probe = tuple(sum(x) for x in zip(moves[i][0], k))
            link = tuple(sum(x) for x in zip(moves[i][1], k))
            nsew.append([probe, link])
        shuffle(nsew)
        for a in nsew:
            probe, link = a
            if probe in el:
                m[probe], m[link] = 1, 1
                el.remove(probe)
                vis.extend(a)
                break
        if n == len(vis):
            k = vis[max(vis.index(k)-1, 1)]
        else:
            k = vis[-1]
    return _get_rooms(m, vis, id_rooms, rules)


def _get_rooms(m, vis, id_rooms, rules):
    rooms = []
    m[vis[0]], m[vis[-2]] = 2, 2
    for coord in vis:
        i, j = coord
        udlr = [m[i-1, j], m[i+1, j], m[i, j-1], m[i, j+1]]
        if udlr in rules:
            rooms.append(coord)
            if id_rooms:
                m[coord] = 2
    return m, rooms


def _draw_maze(m, size):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect(1.0)
    plt.xticks([])
    plt.yticks([])
    plt.pcolormesh(m, cmap=plt.cm.tab20b)
    fig.savefig(
        f"{size}x{size}.png",
        dpi=300,
        bbox_inches="tight",
        pad_inches=-0.1)
    plt.show()


if __name__ == "__main__":
    main(20, draw=True)
