from typing import Self


class Base:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Point(Base):
    """
    Class representing a point in 2D space with x and y coordinates.
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
        """Returns the squared distance between this point and another point.

        Args:
            other: Another Point instance to which the distance is calculated.

        Returns:
            The squared distance as a float.
        """
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2


class Vector(Base):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)
