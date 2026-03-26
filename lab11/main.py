from typing import List, Optional


def is_safe(vertex: int, color: int, colors: List[int], graph: List[List[int]]) -> bool:
    """
    Проверяет, можно ли покрасить вершину vertex в цвет color.
    
    graph — матрица смежности:
    graph[u][v] == 1, если есть ребро между u и v.
    colors[i] == 0 означает, что вершина i ещё не покрашена.
    """
    n = len(graph)
    for neighbor in range(n):
        if graph[vertex][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True


def color_graph_backtracking(
    graph: List[List[int]],
    k: int,
    vertex: int = 0,
    colors: Optional[List[int]] = None
) -> Optional[List[int]]:
    """
    Пытается раскрасить граф в k цветов.
    
    Возвращает список цветов для вершин, если раскраска существует,
    иначе None.
    """
    n = len(graph)

    if colors is None:
        colors = [0] * n

    # База рекурсии: все вершины покрашены
    if vertex == n:
        return colors.copy()

    # Пробуем все цвета от 1 до k
    for color in range(1, k + 1):
        if is_safe(vertex, color, colors, graph):
            colors[vertex] = color

            result = color_graph_backtracking(graph, k, vertex + 1, colors)
            if result is not None:
                return result

            # Откат
            colors[vertex] = 0

    return None


if __name__ == "__main__":
    # Пример графа из 4 вершин
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    k = 4  # Количество цветов для раскраски
    coloring = color_graph_backtracking(graph, k)

    if coloring is None:
        print(f"Граф нельзя раскрасить в {k} цветов")
    else:
        print(f"Раскраска в {k} цветов найдена:")
        for v, c in enumerate(coloring):
            print(f"Вершина {v} -> цвет {c}")