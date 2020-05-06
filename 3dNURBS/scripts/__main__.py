from typing import List

from scripts.nurbs.nurbs import get_NURBS_points
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def get_knots_vec(control_points, spline_deg):
    knot_vector = []
    for i in range(spline_deg):
        knot_vector.append(0)

    m = spline_deg + len(control_points) + 1 - 2 * p
    for i in range(m):
        knot_vector.append(i / (m - 1))

    for i in range(spline_deg):
        knot_vector.append(1)

    return knot_vector

def N(i, p, u, knots: List[float]):
    if p == 0:
        if knots[i] <= u <= knots[i + 1]:
            return 1.
        else:
            return 0.
    return ((u - knots[i]) / (knots[i + p] - knots[i])) * N(i, p - 1, u, knots) + \
           ((knots[i + p + 1] - u) / (knots[i + p + 1] - knots[i + 1])) * N(i + 1, p - 1, u, knots)


def R(i,j,u,v):
    top = N(im)

class Knot:
    def __init__(self, x: float, y: float, z: float, w=1.):
        self.x: float = x
        self.y: float = y
        self.z: float = z
        self.w: float = w


def nurbs_patch_point(knots: List[Knot], u: float, v: float):
    x = 0
    y = 0
    z = 0
    for knot in knots:


def main():
    print("hello", get_NURBS_points(["a", "b"]))
    x = np.linspace(-np.pi, np.pi, 50)
    y = x
    z = np.cos(x)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='parametric curve')
    plt.show()


if __name__ == '__main__':
    main()
