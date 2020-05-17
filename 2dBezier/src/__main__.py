import matplotlib.pyplot as plt

from src.singlebezier.singlebezier import draw_bezier_n
from src.splinebezier.splinebezier import draw_vertex_list


def main():
    vertexes = [
        [1, 1],
        [2, 2],
        [3, 2],
        [5, 3],
        [7, 2],
        [6, 1],
        [8, 4],
        [9, 1],
        [10, 3]
    ]
    vertexes.sort(key=lambda pt: pt[0])
    xs = []
    ys = []
    for p in vertexes:
        xs.append(p[0])
        ys.append(p[1])

    # spline drawer
    # draw_vertex_list(vertexes)

    # single curve drawer
    draw_bezier_n(vertexes)

    plt.scatter(xs, ys)
    plt.show()


if __name__ == '__main__':
    main()
