from typing import Self

import math
import matplotlib.pyplot as plt  # type: ignore


class Point:
    """
    Class representing a point in 2D space with x and y coordinates.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def distance_sq(self, other: Self) -> float:
        """Returns the squared distance between this point and another point.

        Args:
            other: Another Point instance to which the distance is calculated.

        Returns:
            The squared distance as a float.
        """
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2


def orientation(p: Point, q: Point, r: Point) -> float:
    """
    Finds the orientation of ordered triplet (p, q, r).

    Args:
        p : Point
        q : Point.
        r : Point.
    Returns:
        >0, left turn (counter-clockwise),
        <0, right turn (clockwise),
        0, collinear.
    """
    return (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x)


def graham_scan(points: list[Point]) -> list[Point]:
    """Computes the convex hull of a set of points using the Graham scan algorithm.
    Args:
        points: A list of Point objects representing the points (x, y).
    Returns:
        A list of Point objects representing the vertices of the convex hull in counter-clockwise order.
    """
    points = list(set(points))
    n = len(points)
    if n < 2:
        return points
    if n == 2:
        return sorted(points, key=lambda p: (p.y, p.x))

    p0: Point = min(points, key=lambda p: (p.y, p.x))

    def polar_key(point: Point) -> tuple[float, float]:
        dx = point.x - p0.x
        dy = point.y - p0.y
        angle = math.atan2(dy, dx)
        return (angle, p0.distance_sq(point))

    sorted_points = sorted([p for p in points if p != p0], key=polar_key)

    stack = [p0]
    for point in sorted_points:
        while (
            len(stack) >= 2 and orientation(stack[-2], stack[-1], point) <= 0
        ):
            stack.pop()
        stack.append(point)

    return stack


def visualize(points: list[Point], hull: list[Point]) -> None:
    """Visualizes the points and the convex hull using matplotlib.

    Args:
        points: A list of Point objects representing the original points.
        hull: A list of Point objects representing the vertices of the convex hull.
    """

    x_points = [p.x for p in points]
    y_points = [p.y for p in points]
    plt.scatter(x_points, y_points, color='blue', label='Points')

    if len(hull) > 1:
        hull.append(hull[0])
        x_hull = [p.x for p in hull]
        y_hull = [p.y for p in hull]
        plt.plot(x_hull, y_hull, color='red', label='Convex Hull')

    plt.title('Convex Hull Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid()
    plt.show()


def main() -> None:
    points: list[Point] = []

    with open('points.txt', 'r') as file:
        for line in file:
            x, y = map(int, line.split())
            points.append(Point(x, y))

    hull = graham_scan(points)

    visualize(points, hull)


if __name__ == '__main__':
    main()
