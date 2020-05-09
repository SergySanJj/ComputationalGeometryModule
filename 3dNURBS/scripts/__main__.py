from typing import List

from scripts.nurbs.nurbs import get_NURBS_points
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

eps = 0.001


def NN(i, k, u, t):
    if k == 1:
        if t[i] <= u < t[i + 1]:
            return 1
        else:
            return 0

    d1 = (t[i + k - 1] - t[i])
    n1 = (u - t[i])
    s1 = 0
    if d1 != 0 and n1 != 0:
        s1 = n1 * NN(i, k - 1, u, t) / d1

    d2 = (t[i + k] - t[i + 1])
    n2 = (-u + t[i + k])
    s2 = 0
    if d2 != 0 and n2 != 0:
        s2 = n2 * NN(i + 1, k - 1, u, t) / d2

    return s1 + s2


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    knotX = [0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
    knotY = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
    k = len(knotX) - 1
    l = len(knotY) - 1

    vertices3 = [
        [1, 2, 1],
        [2, 3, 1],
        [3, 2, 2],
        [4, 4, 2],
        [5, 1, 2],
        [6, 3, 1],
        [7, 3, 1],
        [9, 1, 0]
    ]

    geom = []
    step = 0.01 * 4
    u = 0.
    while u < 1.:
        w = 0.
        while w < 1:
            vertex = [0, 0, 0]
            for i in range(0, len(vertices3)):
                # for j in range(0, 4):
                #     basis = NN(j, 3, w, knotY)
                #     point_pos = i + j
                #     x = vertices3[point_pos][0]
                #     y = vertices3[point_pos][1]
                #     z = vertices3[point_pos][2]
                #     vertex2[0] += x * basis
                #     vertex2[1] += y * basis
                #     vertex2[2] += z * basis
                x = vertices3[i][0]
                y = vertices3[i][1]
                z = vertices3[i][2]
                basis_x = NN(i, len(knotX) // 2 - 1, u, knotX)
                basis_y = NN(i, len(knotY) // 2 - 1, w, knotY)
                vertex[0] += x * basis_x
                vertex[1] += y * basis_y
                vertex[2] += z * basis_x * basis_y

            geom.append(vertex)
            w += step
        u += step

    xs = []
    ys = []
    zs = []
    for p in geom:
        xs.append(p[0])
        ys.append(p[1])
        zs.append(p[2])

    ax.scatter(xs, ys, zs, label='parametric curve')

    px = []
    py = []
    pz = []
    for p in vertices3:
        px.append(p[0])
        py.append(p[1])
        pz.append(p[2])
        ax.scatter(px, py, pz, label='control points')

    plt.show()


if __name__ == '__main__':
    main()
