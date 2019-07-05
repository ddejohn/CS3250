import matplotlib.pyplot as plt
import numpy
from numpy import zeros as npz
from random import shuffle
from random import choice
from functools import reduce


def main(size=10, draw=False, show_rooms=False, save=False):
    """Generate a square maze.

    Keyword Arguments:

            size : {int} where size % 2 == 0
                dimension of maze (default: {10})
            draw : {bool}
                draw maze as pyplot figure (default: {False})
            show_rooms : {bool}
                show/hide rooms on figure (default: {False})
            save : {bool}
                save figure to CWD as {size}x{size}.png (default: {False})

    Returns:

            maze : {list of list of int}
                a numpy integer matrix
            rooms : {list of tuple}
                a list of the room coordinates as {tuple}
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

    if size % 2 != 0:
        print("Maze size must be an even integer!")
        maze, rooms = None, None
    else:
        maze, rooms = _generate_maze(size, show_rooms, moves, rules)
        if draw:
            _draw_maze(maze, size, save)
    return maze, rooms


def _generate_maze(size, show_rooms, moves, rules):
    m = npz((size+1, size+1), dtype=int)
    nodes = [(a, b) for a in range(1, size+1, 2) for b in range(1, size+1, 2)]
    visited = [choice(nodes)]
    k = visited[0]
    nodes.remove(k)

    while len(nodes) > 0:
        n = len(visited)
        nsew = []
        for i in range(4):
            probe = tuple(sum(x) for x in zip(moves[i][0], k))
            link = tuple(sum(x) for x in zip(moves[i][1], k))
            nsew.append([probe, link])
        shuffle(nsew)
        for a in nsew:
            probe, link = a
            if probe in nodes:
                m[probe], m[link] = 1, 1
                nodes.remove(probe)
                visited.extend(a)
                break
        if n == len(visited):
            k = visited[max(visited.index(k)-1, 1)]
        else:
            k = visited[-1]
    return _get_rooms(m, visited, show_rooms, rules)


def _get_rooms(m, visited, show_rooms, rules):
    rooms = []
    m[visited[0]], m[visited[-2]] = 2, 2
    for coord in visited:
        i, j = coord
        neighbors = [m[i-1, j], m[i+1, j], m[i, j-1], m[i, j+1]]
        if neighbors in rules:
            rooms.append(coord)
            if show_rooms:
                m[coord] = 2
    return m, rooms


def _draw_maze(m, size, save):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect(1.0)
    plt.xticks([])
    plt.yticks([])
    plt.pcolormesh(m, cmap=plt.cm.tab20b)
    if save:
        fig.savefig(
            f"{size}x{size}.png",
            dpi=300,
            bbox_inches="tight",
            pad_inches=-0.1)
    plt.show()


if __name__ == "__main__":
    main(draw=True)
