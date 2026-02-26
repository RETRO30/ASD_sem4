from typing import Self

from .base import Point
from .line import Line


class Polygon:
    def __init__(self, points: list[Point]) -> None:
        self.points = points


class Triangle(Polygon):
    def __init__(self, a: Point, b: Point, c: Point):
        super().__init__([a, b, c])

    def get_edges(self) -> list[Line]:
        return [
            Line(self.points[0], self.points[1], is_segment=True),
            Line(self.points[1], self.points[2], is_segment=True),
            Line(self.points[2], self.points[0], is_segment=True),
        ]

    @property
    def area(self) -> float:
        a, b, c = self.points
        return abs((b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)) / 2

    def is_point_inside(self, point: Point) -> bool:
        a, b, c = self.points
        area_abc = self.area
        area_abp = Triangle(a, b, point).area
        area_acp = Triangle(a, c, point).area
        area_bcp = Triangle(b, c, point).area

        return area_abc == area_abp + area_acp + area_bcp

    def is_nested(self, other: Self) -> bool:
        for point in other.points:
            if not self.is_point_inside(point):
                return False
        return True
