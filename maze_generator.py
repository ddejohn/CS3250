from random import randint as ri
from random import shuffle
from random import choice
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce

size = 100

maze = np.zeros((size+1,size+1), dtype=int)
moves = [(2,0),(0,2),(-2,0),(0,-2)]
el = [(a,b) for a in range(1,size+1,2) for b in range(1,size+1,2)]
vis = [choice(el)]

k = vis[0]
maze[k] = 1
el.remove(k)


def delta(t1,t2):
    x1, y1 = t1
    x2, y2 = t2
    return (x2-x1, y2-y1)


while len(el) > 0:
    n = len(vis)
    nsew = [tuple(sum(x) for x in zip(moves[i], k)) for i in range(4)]
    shuffle(nsew)
    for a in nsew:
        if a in el:
            dxdy = delta(k, a)
            con = [0,0]
            z = reduce(lambda x,y: x if abs(x) > abs(y) else y, dxdy)
            con[dxdy.index(z)] = z//2
            inter = tuple(sum(x) for x in zip(k, tuple(con)))
            vis.append(inter)
            vis.append(a)
            maze[a] = 1
            maze[inter] = 1
            el.remove(a)
            break
    if n == len(vis):
        tail = vis.index(k)
        k = vis[max(tail-1, 1)]
    else:
        shuffle(moves)
        k = vis[len(vis)-1]


# for tup in vis:
#     maze[tup] = 1


plt.figure(figsize=(10, 10))
plt.box(False)
plt.pcolormesh(maze) # cmap=plt.cm.binary)
plt.xticks([])
plt.yticks([])
plt.show()
