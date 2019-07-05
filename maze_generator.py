import matplotlib.pyplot as plt
from numpy import zeros as npz
from random import shuffle
from random import choice
from functools import reduce


def main(size=10, draw=False, rooms=False, save=False):
    """Generate a square maze with 'rooms' on intersections, corners, and dead-ends.

    Keyword Arguments:

            size {int, default: 10} (where size % 2 == 0): unit width of maze
            draw {bool, default: False}: show maze as pyplot figure
            rooms {bool, default: False}: show rooms on figure
            save {bool, default: False}: save figure to working directory as '{size}x{size}.png'

    Returns:

            maze {list of list of int}: a numpy integer matrix
            rooms {list of tuple}: a {list} of room coordinates as {tuple}
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
        maze, nodes = None, None
    else:
        maze, nodes = _generate_maze(size, rooms, moves, rules)
        print(f"Maze contains {len(nodes)} rooms")
        if draw:
            _draw_maze(maze, size, save)
    return maze, nodes


def _generate_maze(size, rooms, moves, rules):
    m = npz((size+1, size+1), dtype=int)
    grid = [(a, b) for a in range(1, size+1, 2) for b in range(1, size+1, 2)]
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
    main(size=16, draw=True)
