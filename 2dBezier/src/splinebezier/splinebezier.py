import matplotlib.pyplot as plt
from typing import List
from math import sqrt

eps = 0.000001


def bezier_coord(points: [List[List[float]]], coord_index: int, t: float) -> float:
    val: float = (1 - t) ** 3 * points[0][coord_index] + \
                 3 * (t - 2 * t ** 2 + t ** 3) * points[1][coord_index] + \
                 3 * (t ** 2 - t ** 3) * points[2][coord_index] + \
                 t ** 3 * points[3][coord_index]
    return val


def bezier_cubic(points: [List[List[float]]], t: float):
    return [bezier_coord(points, 0, t), bezier_coord(points, 1, t)]


def draw_quadratic_bezier(p0, p1, p2, step=0.01):
    line_x = []
    line_y = []
    t = -step
    while t <= 1.0:
        x = quadratic_coord_bezier(p0[0], p1[0], p2[0], t)
        y = quadratic_coord_bezier(p0[1], p1[1], p2[1], t)
        line_x.append(x)
        line_y.append(y)
        t += step
    plt.plot(line_x, line_y)


def quadratic_coord_bezier(p0, p1, p2, t):
    return (1 - t) ** 2 * p0 + 2 * t * (1 - t) * p1 + t ** 2 * p2


def vec_length(vector: List[float]) -> float:
    sum = 0.
    for coord in vector:
        sum += coord ** 2
    return sqrt(sum)


def normalize(vector: List[float]) -> List[float]:
    vec_len = vec_length(vector)
    if abs(vec_len) < eps:
        return [1, 1]
    return [coord / vec_len for coord in vector]


def vectorize(start_point: List[float], end_point: List[float]) -> List[float]:
    res = []
    for i in range(0, 2):
        res.append(end_point[i] - start_point[i])
    return res


def mult(vector: List[float], multiplier: float):
    return [c * multiplier for c in vector]


def turn(points):
    a, b, c = points[0], points[1], points[2]
    return (b[0] - a[1]) * \
           (c[0] - a[0]) - \
           (b[0] - a[0]) * \
           (c[1] - a[1])


def draw_segment(start_point: List[float], end_point: List[float], prev_point: List[float], next_point: List[float]):
    in_vec = normalize(vectorize(prev_point, start_point))
    out_vec = normalize(vectorize(end_point, start_point))
    mid = mult(normalize([
        (in_vec[0] + out_vec[0]) / 2.,
        (in_vec[1] + out_vec[1]) / 2.
    ]), len(vectorize(start_point, end_point)) / 2.)
    s1 = [start_point[0] - mid[0], start_point[1] - mid[1]]

    in_vec = normalize(vectorize(start_point, end_point))
    out_vec = normalize(vectorize(next_point, end_point))
    mid = mult(normalize([
        (in_vec[0] + out_vec[0]) / 2.,
        (in_vec[1] + out_vec[1]) / 2.
    ]), len(vectorize(start_point, end_point)) / 2.)
    s2 = [end_point[0] + mid[0], end_point[1] + mid[1]]

    step = 0.01
    t = 0.0
    segment_x = []
    segment_y = []
    while t <= 1.0:
        coords = bezier_cubic([start_point, s1, s2, end_point], t)
        segment_x.append(coords[0])
        segment_y.append(coords[1])
        t += step
    plt.plot(segment_x, segment_y)
    plt.scatter([s1[0], s2[0]], [s1[1], s2[1]], s=3)


def forwarded_point(start_point: List[float], end_point: List[float], scale=1.) -> List[float]:
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
