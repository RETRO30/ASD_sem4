from typing import Sequence


def color_graph(adjacency: Sequence[Sequence[int]]) -> tuple[int, list[int]]:
    """Решает задачу о раскраске графа.

    Теория:
    - Нужно назначить каждой вершине цвет так, чтобы соседние вершины
      имели разные цвета.
    - Целью является минимизация числа используемых цветов.
    - В данной реализации используется поиск с возвратом (backtracking),
      который перебирает допустимые раскраски с отсечениями.

    Args:
        adjacency: Квадратная матрица смежности графа.

    Returns:
        Кортеж `(chromatic_number, colors)`, где:
        - `chromatic_number` — минимальное число цветов,
        - `colors` — список цветов для вершин, начиная с 0.

    Raises:
        ValueError: Если матрица смежности пуста или не квадратная.
    """
    n = len(adjacency)
    if n == 0:
        raise ValueError("Матрица смежности не должна быть пустой")
    if any(len(row) != n for row in adjacency):
        raise ValueError("Матрица смежности должна быть квадратной")

    degrees = [sum(row) for row in adjacency]
    order = sorted(range(n), key=lambda v: degrees[v], reverse=True)

    best_count = n + 1
    best_colors = [-1] * n
    current_colors = [-1] * n

    def is_valid(vertex: int, color: int) -> bool:
        for neighbor in range(n):
            if adjacency[vertex][neighbor] and current_colors[neighbor] == color:
                return False
        return True

    def backtrack(position: int, used_colors: int) -> None:
        nonlocal best_count, best_colors

        if used_colors >= best_count:
            return

        if position == n:
            best_count = used_colors
            best_colors = current_colors[:]
            return

        vertex = order[position]

        for color in range(used_colors):
            if is_valid(vertex, color):
                current_colors[vertex] = color
                backtrack(position + 1, used_colors)
                current_colors[vertex] = -1

        current_colors[vertex] = used_colors
        backtrack(position + 1, used_colors + 1)
        current_colors[vertex] = -1

    backtrack(0, 0)
    return best_count, best_colors


def main() -> None:
    """Демонстрация задачи о раскраске графа."""
    adjacency = [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [0, 0, 1, 1, 0],
    ]

    chromatic_number, colors = color_graph(adjacency)

    print("Матрица смежности:")
    for row in adjacency:
        print(row)

    print(f"Минимальное число цветов: {chromatic_number}")
    print(f"Раскраска вершин: {colors}")


if __name__ == "__main__":
    main()
