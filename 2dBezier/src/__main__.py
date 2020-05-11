from math import sqrt
from typing import List

import matplotlib
import matplotlib.pyplot as plt

eps = 0.000001


def bezier_coord(points: [List[List[float]]], coord_index: int, t: float) -> float:
    val: float = (1 - t) ** 3 * points[0][coord_index] + \
                 3 * (t - 2 * t ** 2 + t ** 3) * points[1][coord_index] + \
                 3 * (t ** 2 - t ** 3) * points[2][coord_index] + \
                 t ** 3 * points[3][coord_index]
    return val


def bezier_cubic(points: [List[List[float]]], t: float):
    return [bezier_coord(points, 0, t), bezier_coord(points, 1, t)]


def vec_length(vector: List[float]) -> float:
    sum = 0.
    for coord in vector:
        sum += coord ** 2
    return sqrt(sum)


def normalize(vector: List[float]) -> List[float]:
    vec_len = vec_length(vector)
    return [coord / vec_len for coord in vector]


def vectorize(start_point: List[float], end_point: List[float]) -> List[float]:
    res = []
    for i in range(0, 2):
        res.append(end_point[i] - start_point[i])
    return res


def mult(vector: List[float], multiplier: float):
    return [c * multiplier for c in vector]


def draw_segment(start_point: List[float], end_point: List[float], prev_point: List[float], next_point: List[float]):
    in_vec = normalize(vectorize(prev_point, start_point))
    out_vec = normalize(vectorize(start_point, end_point))
    mid = normalize([
        (in_vec[0] + out_vec[0]) / 2.,
        (in_vec[1] + out_vec[1]) / 2.
    ])
    ort = mult(normalize(orthogonal(mid)), vec_length(vectorize(start_point, end_point)) / 3.0)
    s1 = [ort[0] + start_point[0], ort[1] + start_point[1]]

    in_vec = normalize(vectorize(start_point, end_point))
    out_vec = normalize(vectorize(next_point, end_point))
    mid = normalize([
        (in_vec[0] + out_vec[0]) / 2.,
        (in_vec[1] + out_vec[1]) / 2.
    ])
    ort = mult(normalize(orthogonal(mid)), vec_length(vectorize(start_point, end_point)) / 3.0)
    s2 = [ort[0] + end_point[0], ort[1] + end_point[1]]

    step = 0.01
    t = 0.0
    segment_x = []
    segment_y = []
    while t <= 1.0:
        coords = bezier_cubic([start_point, s1, s2, end_point], t)
        segment_x.append(coords[0])
        segment_y.append(coords[1])
        t += step
    plt.scatter(segment_x, segment_y, s=10)


def forwarded_point(start_point: List[float], end_point: List[float], scale=1.01) -> List[float]:
    vec = mult(normalize(vectorize(start_point, end_point)), scale)
    return [vec[0] + end_point[0], vec[1] + end_point[1]]


def draw_vertex_list(vertexes: List[List[float]]):
    t = vertexes
    t.insert(0, forwarded_point(vertexes[1], vertexes[0]))
    t.append(forwarded_point(vertexes[len((vertexes)) - 2], vertexes[len((vertexes)) - 1]))
    ind = 1
    while ind < len(t) - 2:
        draw_segment(t[ind], t[ind + 1], t[ind - 1], t[ind + 2])
        ind += 1


def orthogonal(vector: List[float]) -> List[float]:
    vector_len = vec_length(vector)
    if vector_len < eps:
        return [1, 1]
    return [vector[1] / sqrt(vector[0] ** 2 + vector[1] ** 2),
            -vector[0] / sqrt(vector[0] ** 2 + vector[1] ** 2)]


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

    draw_vertex_list(vertexes)
    plt.show()


if __name__ == '__main__':
    main()
