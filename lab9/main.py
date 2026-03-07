from math import inf, isinf
from typing import Sequence


def solve_tsp(cost: Sequence[Sequence[float]], start: int = 0) -> tuple[float, list[int]]:
    """Решает задачу коммивояжера по матрице связности.

    Используется алгоритм Хелда-Карпа (динамическое программирование по подмножествам).
    Считается кратчайший гамильтонов цикл: старт в `start`, посещение всех городов
    ровно один раз и возврат в старт.

    Args:
        cost: Квадратная матрица стоимостей переходов `n x n`.
              `cost[i][j]` — стоимость перехода из `i` в `j`.
              Для отсутствующего ребра можно использовать `math.inf`.
        start: Индекс стартового города.

    Returns:
        Кортеж `(min_cost, route)`, где:
        - `min_cost` — минимальная стоимость цикла,
        - `route` — маршрут по индексам городов, включая возврат в старт.

    Raises:
        ValueError: Если матрица не квадратная, старт вне диапазона или цикл невозможен.
    """
    n = len(cost)
    if n == 0:
        raise ValueError("Матрица связности не должна быть пустой")

    if start < 0 or start >= n:
        raise ValueError("Некорректный индекс стартового города")

    if any(len(row) != n for row in cost):
        raise ValueError("Матрица связности должна быть квадратной")

    # Перенумеровываем города так, чтобы стартовый был с индексом 0.
    order = [start] + [city for city in range(n) if city != start]
    index_of = {city: idx for idx, city in enumerate(order)}

    reordered = [[0.0] * n for _ in range(n)]
    for i_old in range(n):
        for j_old in range(n):
            i_new = index_of[i_old]
            j_new = index_of[j_old]
            reordered[i_new][j_new] = float(cost[i_old][j_old])

    full_mask = (1 << n) - 1

    # dp[mask][j] = минимальная стоимость пути 0 -> ... -> j,
    # где посещены города из mask (бит j обязательно выставлен).
    dp = [[inf] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    dp[1][0] = 0.0

    for mask in range(1 << n):
        if (mask & 1) == 0:
            continue

        for last in range(n):
            if (mask & (1 << last)) == 0 or isinf(dp[mask][last]):
                continue

            for nxt in range(1, n):
                if mask & (1 << nxt):
                    continue

                edge = reordered[last][nxt]
                if isinf(edge):
                    continue

                new_mask = mask | (1 << nxt)
                candidate = dp[mask][last] + edge
                if candidate < dp[new_mask][nxt]:
                    dp[new_mask][nxt] = candidate
                    parent[new_mask][nxt] = last

    min_cost = inf
    last_city = -1
    for j in range(1, n):
        if isinf(dp[full_mask][j]) or isinf(reordered[j][0]):
            continue

        tour_cost = dp[full_mask][j] + reordered[j][0]
        if tour_cost < min_cost:
            min_cost = tour_cost
            last_city = j

    if n == 1:
        return 0.0, [start, start]

    if last_city == -1:
        raise ValueError("Гамильтонов цикл не существует для данной матрицы")

    # Восстановление маршрута в перенумерованной системе индексов.
    route_reordered = [0]
    mask = full_mask
    current = last_city
    stack = [current]

    while current != 0:
        prev = parent[mask][current]
        mask ^= 1 << current
        current = prev
        stack.append(current)

    stack.reverse()  # [0, ..., last_city]
    route_reordered = stack + [0]

    # Возврат к исходной нумерации городов.
    route_original = [order[idx] for idx in route_reordered]
    return min_cost, route_original


def main() -> None:
    """Демонстрация решения задачи коммивояжера."""
    matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    min_cost, route = solve_tsp(matrix, start=0)

    print("Матрица связности:")
    for row in matrix:
        print(row)

    print(f"Минимальная стоимость маршрута: {min_cost}")
    print(f"Маршрут: {route}")


if __name__ == "__main__":
    main()
