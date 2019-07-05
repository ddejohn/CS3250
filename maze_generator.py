import matplotlib.pyplot as plt
from numpy import zeros as npz
from numpy import where as npw
from random import shuffle
from random import choice
from random import randint
from functools import reduce


def main(size, id_rooms=False):
    moves = [(0,2),(0,-2),(-2,0),(2,0)]
    neighbors = [(0,1),(0,-1),(-1,0),(1,0)] # U, D, L, R
    maze = npz((size+1,size+1), dtype=int)
    el = [(a,b) for a in range(1,size+1,2) for b in range(1,size+1,2)]
    vis = [choice(el)]

    k = vis[0]
    maze[k] = 1
    el.remove(k)

    def delta(t1,t2):
        x1, y1 = t1
        x2, y2 = t2
        return (x2-x1, y2-y1)

    def get_links(a, k):
        con = [0,0]
        dxdy = delta(k, a)
        z = reduce(lambda x,y: x if abs(x) > abs(y) else y, dxdy)
        con[dxdy.index(z)] = z//2
        inter = tuple(sum(x) for x in zip(k, tuple(con)))
        return inter, a

    def get_rooms(m):
        rules = [
            [0,0,0,1],  # left end-cap
            [0,0,1,0],  # right end-cap
            [0,1,0,0],  # top end-cap
            [1,0,0,0],  # bottom end-cap
            [1,1,1,0],  # left 3-way
            [1,1,0,1],  # right 3-way
            [1,0,1,1],  # top 3-way
            [0,1,1,1],  # bottom 3-way
            [1,1,1,1],  # 4-way
            [1,0,1,0],  # up-left corner
            [1,0,0,1],  # up-right corner
            [0,1,1,0],  # down-left corner
            [0,1,0,1],  # down-right corner
        ]

        dim = m.shape[0]
        rnge = range(1, dim-1)
        rooms = []
        top_rooms = []
        bottom_rooms = []
        for i in rnge:
            for j in rnge:
                if m[i,j] == 1:
                    udlr = [m[i-1,j], m[i+1,j], m[i,j-1], m[i,j+1]]
                    if udlr in rules:
                        if id_rooms:
                            m[i,j] = -1
                        rooms.append((i,j))
        for room in rooms:
            if room[0] == 1:
                top_rooms.append(room)
            elif room[0] == dim-2:
                bottom_rooms.append(room)

        return m, [rooms, top_rooms, bottom_rooms]

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

    while len(el) > 0:
        n = len(vis)
        nsew = [tuple(sum(x) for x in zip(moves[i], k)) for i in range(4)]
        shuffle(nsew)
        for a in nsew:
            if a in el:
                inter, a = get_links(a, k)
                vis.extend([inter, a])
                maze[inter], maze[a] = 1, 1
                el.remove(a)
                break
        if n == len(vis):
            k = vis[max(vis.index(k)-1, 1)]
        else:
            k = vis[len(vis)-1]

    maze, rooms = get_rooms(maze)
    rooms, top_rooms, bottom_rooms = rooms
    maze = make_soln(maze, top_rooms, bottom_rooms)
    print(len(rooms))

    fig = plt.figure(figsize=(20, 20))
    plt.box(False)
    plt.pcolormesh(maze)    # cmap=plt.cm.magma
    plt.xticks([])
    plt.yticks([])
    plt.axes().set_aspect('equal')
    fig.savefig(
        f"{size}x{size}.png",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0)
    plt.show()


if __name__ == "__main__":
    main(50, id_rooms=False)