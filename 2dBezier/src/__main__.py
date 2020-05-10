from typing import List

import matplotlib


def bezier_coord(points: [List[List[float]]], coord_index: int, t: float) -> float:
    val: float = (1 - t) ** 3 * points[0][coord_index] + \
                 3 * (t - 2 * t ** 2 + t ** 3) * points[1][coord_index] + \
                 3 * (t ** 2 - t ** 3) * points[2][coord_index] + \
                 t ** 3 * points[3][coord_index]
    return val


def bezier_cubic(points: [List[List[float]]], t: float):
    return [bezier_coord(points, 0, t), bezier_coord(points, 1, t)]


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

    print("hi")


if __name__ == '__main__':
    main()
