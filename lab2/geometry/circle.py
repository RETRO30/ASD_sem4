from .base import Point


class Circle:
    """Окружность на плоскости.

    Теория:
    - Окружность с центром `C(x0, y0)` и радиусом `r` задается уравнением
      `(x - x0)^2 + (y - y0)^2 = r^2`.
    - Радиус определяет множество точек, равноудаленных от центра.
    """

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius
