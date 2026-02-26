from geometry import Point, Vector, Line, Circle, Triangle
from geometry.intersection import Intersection


def generate_triangles(points: list[Point]) -> list[Triangle]:
    triangles = []
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                triangles.append(Triangle(points[i], points[j], points[k]))

    return triangles


# def visualize(
#     points: list[Point], nested_triangles: list[tuple[Triangle, Triangle]]
# ) -> None:
#     import matplotlib.pyplot as plt

#     plt.figure(figsize=(8, 8))
#     plt.scatter(
#         [p.x for p in points],
#         [p.y for p in points],
#         color='blue',
#         label='Points',
#     )

#     for outer, inner in nested_triangles:
#         outer_x = [p.x for p in outer.points] + [outer.points[0].x]
#         outer_y = [p.y for p in outer.points] + [outer.points[0].y]
#         inner_x = [p.x for p in inner.points] + [inner.points[0].x]
#         inner_y = [p.y for p in inner.points] + [inner.points[0].y]

#         plt.plot(outer_x, outer_y, color='red', label='Outer Triangle')
#         plt.plot(inner_x, inner_y, color='green', label='Inner Triangle')

#     plt.legend()
#     plt.title('Nested Triangles Visualization')
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
#     plt.grid()
#     plt.show()


if __name__ == '__main__':
    points: list[Point] = []

    with open('points.txt') as f:
        for line in f:
            x, y = map(float, line.split())
            points.append(Point(x, y))

    triangles = generate_triangles(points)

    nested_triangles = []
    for triangle in triangles:
        for other in triangles:
            if triangle != other and triangle.is_nested(other):
                nested_triangles.append((triangle, other))

    print(f'Generated {len(triangles)} triangles')

    print(f'Found {len(nested_triangles)} nested triangle pairs')

    # visualize(points, nested_triangles)
