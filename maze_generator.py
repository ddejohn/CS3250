import matplotlib.pyplot as plt
from numpy import zeros as npz
from random import shuffle
from random import choice
from functools import reduce


def main(dims=(10, 10), draw=False, rooms=False, save=False):
    """Generate a maze with 'rooms' on intersections, corners, and dead-ends.

    Keyword Arguments:

            dims {tuple, default: (x=10, y=10)} (where x + y % 2 == 0):
                unit dimensions of maze
            
            draw {bool, default: False}:
                show maze as pyplot figure
            
            rooms {bool, default: False}:
                highlight rooms on figure
            
            save {bool, default: False}:
                save figure to working directory as png

    Returns:

            maze {list of list of int}:
                a numpy integer matrix

            rooms {list of tuple}:
                a {list} of room coordinates as {tuple}
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

    if sum(dims) % 2 != 0:
        print("Maze dimensions must be even integers!")
        maze, nodes = None, None
    else:
        maze, nodes = _generate_maze(dims, rooms, moves, rules)
        print(f"Maze contains {len(nodes)} rooms")
        if draw:
            _draw_maze(maze, len(nodes), save)
    return maze, nodes


def _generate_maze(dims, rooms, moves, rules):
    x, y = dims
    m = npz((x+1, y+1), dtype=int)
    grid = [(a, b) for a in range(1, x+1, 2) for b in range(1, y+1, 2)]
    visited = [choice(grid)]
    k = visited[0]
    grid.remove(k)

    while len(grid) > 0:
        n = len(visited)
        nsew = []
        for i in range(4):
            probe = tuple(sum(x) for x in zip(moves[i][0], k))
            link = tuple(sum(x) for x in zip(moves[i][1], k))
            nsew.append([probe, link])
        shuffle(nsew)
        for a in nsew:
            probe, link = a
            if probe in grid:
                m[probe], m[link] = 1, 1
                grid.remove(probe)
                visited.extend(a)
                break
        if n == len(visited):
            k = visited[max(visited.index(k)-1, 1)]
        else:
            k = visited[-1]
    return _get_rooms(m, visited, rooms, rules)


def _get_rooms(m, visited, rooms, rules):
    nodes = []
    m[visited[0]], m[visited[-2]] = 2, 2
    for coord in visited:
        i, j = coord
        neighbors = [m[i-1, j], m[i+1, j], m[i, j-1], m[i, j+1]]
        if neighbors in rules:
            nodes.append(coord)
            if rooms:
                m[coord] = 2
    return m, nodes


def _draw_maze(m, rooms, save):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect(1.0)
    plt.xticks([])
    plt.yticks([])
    plt.pcolormesh(m, cmap=plt.cm.tab20b)
    if save:
        fig.savefig(
            f"{m.shape[0]-1}x{m.shape[1]-1}_{rooms}_rooms.png",
            dpi=300,
            bbox_inches="tight",
            pad_inches=-0.1)
    plt.show()


if __name__ == "__main__":
    main(dims=(6, 20), draw=True, rooms=False, save=False)
