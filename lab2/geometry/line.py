from .base import Point, Vector
import math


class Line:
    """Прямая или отрезок, заданный двумя точками.

    Теория:
    - Параметрическое уравнение: `P(t) = P1 + t * (P2 - P1)`.
    - Для бесконечной прямой `t` принимает любые вещественные значения.
    - Для отрезка `t` ограничен интервалом `[0, 1]`.
    """

    def __init__(self, p1: Point, p2: Point, is_segment: bool = True):
        self.p1 = p1
        self.p2 = p2
        self.is_segment = is_segment

    @property
    def length(self) -> float | None:
        """Возвращает длину отрезка.

        Для бесконечной прямой длина не определена, поэтому возвращается `None`.
        """
        if not self.is_segment:
            return None
        return math.sqrt(self.p1.distance_sq(self.p2))

    def get_vector(self) -> Vector:
        """Возвращает направляющий вектор от `p1` к `p2`: `(x2 - x1, y2 - y1)`."""
        return Vector(self.p2.x - self.p1.x, self.p2.y - self.p1.y)
