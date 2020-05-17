from typing import List, Tuple

import matplotlib.pyplot as plt

eps = 0.0000001


def N(i: int, p: int, cur_u: float, K: List[float]) -> float:
    if p == 0:
        if K[i] <= cur_u < K[i + 1]:
            return 1.0
        else:
            return 0.0

    d1 = K[i + p] - K[i]
    if abs(d1) < eps:
        s1 = 0.
    else:
        basis_blending = N(i, p - 1, cur_u, K)
        s1 = (cur_u - K[i]) / d1 * basis_blending

    d2 = (K[i + p + 1] - K[i + 1])
    if abs(d2) < eps:
        s2 = 0.
    else:
        basis_blending = N(i + 1, p - 1, cur_u, K)
        s2 = (K[i + p + 1] - cur_u) / d2 * basis_blending

    return s1 + s2


def create_patch(points: List[List[float]],
                 knot_x: List[float],
                 knot_y: List[float],
                 order: int, step=0.08) -> Tuple[List[float], List[float], List[float]]:
    surf_x = []
    surf_y = []
    surf_z = []

    u = 0.0
    while u <= 1.0:
        v = 0.0
        while v <= 1.0:
            x = 0.0
            y = 0.0
            z = 0.0
            divider = 0.0
            for i in range(2):
                for j in range(2):
                    i_basis = N(i, order, u, knot_x)
                    j_basis = N(j, order, v, knot_y)
                    ind = i * 2 + j
                    x += i_basis * j_basis * points[ind][0]
                    y += i_basis * j_basis * points[ind][1]
                    z += i_basis * j_basis * points[ind][2]
                    divider += i_basis * j_basis

            if abs(divider) > eps:
                surf_x.append(x / divider)
                surf_y.append(y / divider)
                surf_z.append(z / divider)
            v += step

        u += step
    return surf_x, surf_y, surf_z


def draw_nurbs_surface(points: List[List[float]],
                       knot_x: List[float],
                       knot_y: List[float],
                       order: int, step=0.08):
    plt.figure()
    ax = plt.axes(projection='3d')

    curr_pos = 0
    while curr_pos + 4 <= len(points):
        ax.scatter(*create_patch(points[curr_pos:curr_pos + 4], knot_x, knot_y, order))
        curr_pos += 2

    plt.show()
