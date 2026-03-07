from typing import Self


class Base:
    """Базовый класс для объектов с декартовыми координатами `(x, y)`.

    В аналитической геометрии точка или вектор на плоскости задаются
    парой вещественных чисел в системе координат OXY.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Point(Base):
    """Точка на плоскости.

    Теория:
    - Точка определяет положение в пространстве и не имеет размеров.
    - Расстояние между точками `A(x1, y1)` и `B(x2, y2)`:
      `|AB| = sqrt((x2 - x1)^2 + (y2 - y1)^2)`.
    - В вычислениях часто используют квадрат расстояния, чтобы избежать
      лишнего извлечения корня.
    """

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def distance_sq(self, other: Self) -> float:
        """Возвращает квадрат расстояния до другой точки.

        Формула: `(x1 - x2)^2 + (y1 - y2)^2`.
        """
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2


class Vector(Base):
    """Вектор на плоскости в координатной форме `(x, y)`.

    Теория:
    - Вектор задает направление и длину.
    - Длина вектора `v = (x, y)` равна `|v| = sqrt(x^2 + y^2)`.
    - В этой лабораторной векторы применяются для параметрических уравнений
      прямых и вычисления пересечений.
    """

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)
