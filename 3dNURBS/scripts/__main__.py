from nurbs.nurbs import draw_nurbs_surface


def main():
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
    knot_x = knot_y = [0.0, 0.0, 0.0, 0.5, 0.75, 0.9, 1.0]

    draw_nurbs_surface(points=vertexes, knot_x=knot_x, knot_y=knot_y, order=order)


if __name__ == '__main__':
    main()
