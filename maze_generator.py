import matplotlib.pyplot as plt
from numpy import zeros as npz
from random import shuffle
from random import choice
from functools import reduce


def main(size):
    moves = [(2,0),(0,2),(-2,0),(0,-2)]
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

    plt.figure(figsize=(10, 10))
    plt.box(False)
    plt.pcolormesh(maze) # cmap=plt.cm.binary)
    plt.xticks([])
    plt.yticks([])
    plt.show()


if __name__ == "__main__":
    main(12)