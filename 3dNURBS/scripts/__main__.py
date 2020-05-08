from typing import List

from scripts.nurbs.nurbs import get_NURBS_points
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def N(i, k, t, u):
    if k == 1:
        if u[i] <= t <= u[i + 1]:
            return 1
        else:
            return 0

    if u[i + k - 1] - u[i]:
        term_left = ((t - u[i]) * N(i, k - 1, t, u)) / (u[i + k - 1] - u[i])
    else:
        term_left = 0

    if u[i + k] - u[i + 1]:
        term_right = ((u[i + k] - t) * N(i + 1, k - 1, t, u)) / (u[i + k] - u[i + 1])
    else:
        term_right = 0

    return term_left + term_right


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    k = 4
    l = 3
    knotX = [0, 0, 0, 0, 1, 1, 1, 1]
    knotY = [0, 0, 0, 1, 2, 2, 2]

    vertices3 = [
        [-15, 0, 15],
        [-5, 5, 15],
        [5, 5, 15],
        [15, 0, 15],

        [-15, 5, 5],
        [-5, 10, 5],
        [5, 10, 5],
        [15, 5, 5],

        [-15, 5, -5],
        [-5, 10, -5],
        [5, 10, -5],
        [15, 5, -5],

        [-15, 0, -15],
        [-5, 5, -15],
        [5, 5, -15],
        [15, 0, -15]
    ]

    geom = []
    step = 0.01 * 4
    u = 0.
    while u < 1.:
        w = 0.
        while w < 2:
            vertex = [0, 0, 0]
            for i in range(0, 4):
                vertex2 = [0, 0, 0]
                for j in range(0, 4):
                    basis = N(j, l, w, knotY)
                    point_pos = 4 * j + i
                    x = vertices3[point_pos][0]
                    y = vertices3[point_pos][1]
                    z = vertices3[point_pos][2]
                    vertex2[0] += x * basis
                    vertex2[1] += y * basis
                    vertex2[2] += z * basis

                basis = N(i, k, u, knotX)
                x, y, z = vertex2[0], vertex2[1], vertex2[2]
                vertex[0] += x * basis
                vertex[1] += y * basis
                vertex[2] += z * basis

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

    ax.plot(xs, ys, zs, label='parametric curve')
    xs = [x + 1. for x in xs]
    ax.plot(xs, ys, zs, label='parametric curve')

    plt.show()


if __name__ == '__main__':
    main()
