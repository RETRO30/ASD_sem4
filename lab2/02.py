import math

EPS = 1e-9


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


def cross(a, b):
    return a.x * b.y - a.y * b.x


def dot(a, b):
    return a.x * b.x + a.y * b.y


def distance(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)


def is_zero(value):
    return abs(value) <= EPS


def same_point(a, b):
    return is_zero(a.x - b.x) and is_zero(a.y - b.y)


def orientation(a, b, c):
    return cross(b - a, c - a)


def is_point_on_segment(p, a, b):
    # Проверка коллинеарности
    if not is_zero(orientation(a, b, p)):
        return False
    # Проверка проекций
    return min(a.x, b.x) - EPS <= p.x <= max(a.x, b.x) + EPS and min(
        a.y, b.y
    ) - EPS <= p.y <= max(a.y, b.y) + EPS


def intersect_lines(p1, p2, p3, p4):
    # Ищет точку пересечения двух бесконечных прямых.
    v1 = p2 - p1
    v2 = p4 - p3

    det = cross(v1, v2)

    if is_zero(det):
        return None
    t = cross(p3 - p1, v2) / det

    return p1 + v1 * t


def intersection_line_segment(l1, l2, s1, s2):
    # Ищет пересечение бесконечной прямой и отрезка.
    point = intersect_lines(l1, l2, s1, s2)

    if point is None:
        return None
    if is_point_on_segment(point, s1, s2):
        return point

    return None


def intersection_segments(a, b, c, d):
    # Ищет пересечение двух отрезков.
    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)

    if o1 * o2 < 0 and o3 * o4 < 0:
        v1 = b - a
        v2 = d - c
        t = cross(c - a, v2) / cross(v1, v2)
        return [a + v1 * t]

    collinear_point = []
    if is_zero(o1) and is_point_on_segment(c, a, b):
        collinear_point.append(c)
    if is_zero(o2) and is_point_on_segment(d, a, b):
        collinear_point.append(d)
    if is_zero(o3) and is_point_on_segment(a, c, d):
        collinear_point.append(a)
    if is_zero(o4) and is_point_on_segment(b, c, d):
        collinear_point.append(b)
    uniq_points = []

    for p in collinear_point:
        if not any(same_point(p, up) for up in uniq_points):
            uniq_points.append(p)

    if len(uniq_points) == 2:
        return sorted(uniq_points, key=lambda p: (p.x, p.y))
    elif len(uniq_points) == 1:
        return uniq_points

    return None


def intersect_line_circle(p1, p2, center, r):
    # Ищет точки пересечения бесконечной прямой и окружности.
    o1 = p1 - center
    o2 = p2 - center

    d = o2 - o1

    a = dot(d, d)
    b = 2 * dot(o1, d)
    c = dot(o1, o1) - r**2

    D = b**2 - 4 * a * c
    if D < -EPS:
        return []
    if is_zero(D):
        t = -1 * b / (2 * a)
        point = o1 + d * t
        return [point + center]
    sqrt_D = math.sqrt(D)
    t1 = (-1 * b - sqrt_D) / (2 * a)
    t2 = (-1 * b + sqrt_D) / (2 * a)

    point1 = o1 + d * t1
    point2 = o1 + d * t2

    return [point1 + center, point2 + center]


def intersection_segment_circle(a, b, center, r):
    # Оставляет только те точки пересечения, которые лежат на отрезке.
    points = intersect_line_circle(a, b, center, r)
    result = []

    for point in points:
        if is_point_on_segment(point, a, b):
            if not any(same_point(point, saved) for saved in result):
                result.append(point)

    return result


def intersect_circles(c1, r1, c2, r2):
    # Ищет точки пересечения двух окружностей.
    d = distance(c1, c2)

    if d > r1 + r2 + EPS:
        return []
    if d < abs(r1 - r2) - EPS:
        return []
    if is_zero(d) and is_zero(r1 - r2):
        return []

    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h_sq = r1**2 - a**2

    if h_sq < -EPS:
        return []
    if h_sq < 0:
        h_sq = 0

    base = Point(c1.x + a * (c2.x - c1.x) / d, c1.y + a * (c2.y - c1.y) / d)

    if is_zero(h_sq):
        return [base]

    h = math.sqrt(h_sq)
    rx = -(c2.y - c1.y) * h / d
    ry = (c2.x - c1.x) * h / d

    return [
        Point(base.x + rx, base.y + ry),
        Point(base.x - rx, base.y - ry),
    ]


def triangle_area(a, b, c):
    return abs(orientation(a, b, c)) / 2


def is_point_in_triangle(p, a, b, c):
    # Проверяет, лежит ли точка внутри треугольника или на его границе.
    area = triangle_area(a, b, c)

    if is_zero(area):
        return False

    area1 = triangle_area(p, a, b)
    area2 = triangle_area(p, b, c)
    area3 = triangle_area(p, c, a)

    return is_zero(area - area1 - area2 - area3)


def is_nested_triangle(outer, inner):
    for point in inner:
        if not is_point_in_triangle(point, outer[0], outer[1], outer[2]):
            return False
    return True


def find_nested_triangles(points):
    triangles = []
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if not is_zero(triangle_area(points[i], points[j], points[k])):
                    triangles.append((points[i], points[j], points[k]))

    nested = []
    for i in range(len(triangles)):
        for j in range(len(triangles)):
            if i != j and is_nested_triangle(triangles[i], triangles[j]):
                nested.append((triangles[i], triangles[j]))

    return nested


def format_points(points):
    if points is None:
        return 'None'
    if len(points) == 0:
        return '[]'
    return '[' + ', '.join(str(point) for point in points) + ']'


def main():
    l1 = Point(0, 0)
    l2 = Point(4, 4)
    l3 = Point(0, 4)
    l4 = Point(4, 0)

    s1 = Point(1, 3)
    s2 = Point(5, 3)

    c1 = Point(2, 2)
    r1 = 2
    c2 = Point(5, 2)
    r2 = 2

    points = [
        Point(0, 0),
        Point(6, 0),
        Point(0, 6),
        Point(1, 1),
        Point(2, 1),
        Point(1, 2),
        Point(7, 7),
    ]

    print('Пересечение двух прямых:')
    print(intersect_lines(l1, l2, l3, l4))

    print('\nПересечение прямой и отрезка:')
    print(intersection_line_segment(l1, l2, s1, s2))

    print('\nПересечение двух отрезков:')
    print(format_points(intersection_segments(l1, l2, l3, l4)))

    print('\nПересечение прямой и окружности:')
    print(format_points(intersect_line_circle(l1, l2, c1, r1)))

    print('\nПересечение отрезка и окружности:')
    print(format_points(intersection_segment_circle(l1, l2, c1, r1)))

    print('\nПересечение двух окружностей:')
    print(format_points(intersect_circles(c1, r1, c2, r2)))

    print('\nВложенные треугольники:')
    nested = find_nested_triangles(points)
    print(f'Найдено пар: {len(nested)}')
    for outer, inner in nested:
        print('Внешний:', format_points(outer))
        print('Внутренний:', format_points(inner))
        print()


if __name__ == '__main__':
    main()
