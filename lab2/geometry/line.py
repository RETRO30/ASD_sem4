from .base import Point, Vector
import math


class Line:
    def __init__(self, p1: Point, p2: Point, is_segment: bool = True):
        self.p1 = p1
        self.p2 = p2
        self.is_segment = is_segment

    @property
    def length(self) -> float | None:
        """Get lenght

        Returns:
            float: lenght
            None: is not segment
        """
        if not self.is_segment:
            return None
        return math.sqrt(self.p1.distance_sq(self.p2))

    def get_vector(self) -> Vector:
        """Get vector a -> b

        Returns:
            Vector: vector a -> b
        """
        return Vector(self.p2.x - self.p1.x, self.p2.y - self.p1.y)
