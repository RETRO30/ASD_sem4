from . import Point, Vector, Line, Circle, Triangle
from typing import Optional


class Intersection:
    @staticmethod
    def line_to_line(a: Line, b: Line) -> Optional[Point | Line]:
        d1: Vector = a.get_vector()
        d2: Vector = b.get_vector()
        d3: Vector = Line(a.p1, b.p1).get_vector()

        det = d2.x * d1.y - d2.y * d1.x

        if det == 0:
            if d2.x * d3.y - d2.y * d3.x == 0:
                return Line(
                    max(a.p1, a.p2, b.p1, b.p2, key=lambda p: (p.x, p.y)),
                    min(a.p1, a.p2, b.p1, b.p2, key=lambda p: (p.x, p.y)),
                )
            else:
                return None
        t1 = (d2.x * d3.y - d2.y * d3.x) / det
        t2 = (d1.x * d3.y - d1.y * d3.x) / det

        if a.is_segment and (t1 < 0 or t1 > 1):
            return None
        if b.is_segment and (t2 < 0 or t2 > 1):
            return None
        return Point(a.p1.x + t1 * d1.x, a.p1.y + t1 * d1.y)

    @staticmethod
    def line_to_circle(line: Line, circle: Circle) -> Optional[list[Point]]:
        # Vector from circle center to line start point
        to_p1 = Vector(
            line.p1.x - circle.center.x, line.p1.y - circle.center.y
        )
        line_dir = line.get_vector()

        # Coefficients for quadratic equation
        a = line_dir.x**2 + line_dir.y**2
        b = 2 * (to_p1.x * line_dir.x + to_p1.y * line_dir.y)
        c = to_p1.x**2 + to_p1.y**2 - circle.radius**2

        discriminant = b**2 - 4 * a * c

        if discriminant < 0:
            return None

        sqrt_disc = discriminant**0.5
        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)

        points = []
        for t in [t1, t2]:
            if line.is_segment and (t < 0 or t > 1):
                continue
            points.append(
                Point(line.p1.x + t * line_dir.x, line.p1.y + t * line_dir.y)
            )

        return points if points else None

    @staticmethod
    def circle_to_cirlce(a: Circle, b: Circle) -> Optional[list[Point]]:
        d = a.center.distance_sq(b.center) ** 0.5
        if d > a.radius + b.radius or d < abs(a.radius - b.radius):
            return None

        if d == 0 and a.radius == b.radius:
            return None

        a_to_b = Vector(b.center.x - a.center.x, b.center.y - a.center.y)
        a_to_b_len = (a_to_b.x**2 + a_to_b.y**2) ** 0.5
        a_to_b_unit = Vector(a_to_b.x / a_to_b_len, a_to_b.y / a_to_b_len)

        x = (a.radius**2 - b.radius**2 + d**2) / (2 * d)
        y = (a.radius**2 - x**2) ** 0.5

        mid_point = Point(
            a.center.x + x * a_to_b_unit.x, a.center.y + x * a_to_b_unit.y
        )

        if y == 0:
            return [mid_point]

        offset = Vector(-y * a_to_b_unit.y, y * a_to_b_unit.x)
        return [
            Point(mid_point.x + offset.x, mid_point.y + offset.y),
            Point(mid_point.x - offset.x, mid_point.y - offset.y),
        ]

    @staticmethod
    def triangle_to_triangle(
        a: Triangle, b: Triangle
    ) -> Optional[list[Point]]:
        points = set()

        for line_a in a.get_edges():
            for line_b in b.get_edges():
                inter = Intersection.line_to_line(line_a, line_b)
                if isinstance(inter, Point):
                    points.add(inter)

        return list(points) if points else None
