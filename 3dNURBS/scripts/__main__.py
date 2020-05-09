from typing import List, Tuple

import numpy as np
import matplotlib.pyplot as plt

eps = 0.00001


def N(i: int, p: int, cur_u: float, arr_u: List[float]) -> float:
    if p == 0:
        if arr_u[i] <= cur_u < arr_u[i + 1]:
            return 1.0
        else:
            return 0.0

    d1 = arr_u[i + p] - arr_u[i]
    if abs(d1) < eps:
        s1 = 0.
    else:
        basis = N(i, p - 1, cur_u, arr_u)
        s1 = (cur_u - arr_u[i]) / d1 * basis

    d2 = (arr_u[i + p + 1] - arr_u[i + 1])
    if abs(d2) < eps:
        s2 = 0.
    else:
        basis = N(i + 1, p - 1, cur_u, arr_u)
        s2 = (arr_u[i + p + 1] - cur_u) / d2 * basis

    return s1 + s2


def create_patch(points: List[List[float]], step=0.08) -> Tuple[List[float], List[float], List[float]]:
    surf_x = []
    surf_y = []
    surf_z = []

    u = 0.0
    while u <= 1.0:
        v = 0.0
        while v <= 1.0:
            count_top_x = 0.0
            count_top_y = 0.0
            count_top_z = 0.0
            count_down = 0.0
            for i in range(2):
                for j in range(2):
                    Bip = N(i, order, u, U)
                    Bjp = N(j, order, v, V)
                    ind = i * 2 + j
                    count_top_x += Bip * Bjp * points[ind][0]
                    count_top_y += Bip * Bjp * points[ind][1]
                    count_top_z += Bip * Bjp * points[ind][2]
                    count_down += Bip * Bjp

            if count_down != 0:
                surf_x.append(count_top_x / count_down)
                surf_y.append(count_top_y / count_down)
                surf_z.append(count_top_z / count_down)
            v += step

        u += step
    return surf_x, surf_y, surf_z


if __name__ == '__main__':
    vertexes = [
        [1, 2, 1],
        [2, 3, 1],
        [3, 2, 2],
        [4, 4, 2],
        [5, 1, 2],
        [6, 3, 1],
        [7, 3, 1],
        [9, 1, 0]
    ]

    order = 4

    U = V = [0.0, 0.0, 0.0, 0.5, 0.75, 0.9, 1.0]

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.scatter(*create_patch(vertexes[4:8]))
    ax.scatter(*create_patch(vertexes[2:6]))
    ax.scatter(*create_patch(vertexes[0:4]))

    plt.show()
