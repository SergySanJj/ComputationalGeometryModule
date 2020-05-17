import matplotlib.pyplot as plt

eps = 0.000001


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def bernstein_basis(k, n, t):
    return combinations(n, k) * t ** k * (1 - t) ** (n - k)


def bezier_n(vertexes, t):
    x = 0.
    y = 0.
    k = 0
    n = len(vertexes)
    while k < n:
        b = bernstein_basis(k, n - 1, t)
        x += vertexes[k][0] * b
        y += vertexes[k][1] * b

        k += 1
    return x, y


def draw_bezier_n(vertexes, step=0.01):
    t = 0.
    xs = []
    ys = []
    while t <= 1. + step:
        x, y = bezier_n(vertexes, t)
        xs.append(x)
        ys.append(y)
        t += step
    plt.plot(xs, ys)