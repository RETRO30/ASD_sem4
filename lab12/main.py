from typing import Sequence


def solve_knapsack(
    capacity: int,
    weights: Sequence[int],
    values: Sequence[int],
) -> tuple[int, list[int]]:
    """Решает дискретную задачу о рюкзаке.

    Теория:
    - В задаче 0/1-рюкзака каждый предмет можно либо взять целиком, либо не брать.
    - Нужно максимизировать суммарную стоимость предметов при ограничении
      на общий вес.
    - Динамическое программирование использует таблицу `dp[i][w]`:
      максимальная стоимость, достижимая первыми `i` предметами
      при вместимости `w`.

    Args:
        capacity: Вместимость рюкзака.
        weights: Веса предметов.
        values: Стоимости предметов.

    Returns:
        Кортеж `(max_value, chosen_items)`, где:
        - `max_value` — максимальная суммарная стоимость,
        - `chosen_items` — индексы выбранных предметов.

    Raises:
        ValueError: Если входные данные некорректны.
    """
    if capacity < 0:
        raise ValueError("Вместимость рюкзака не может быть отрицательной")
    if len(weights) != len(values):
        raise ValueError("Количество весов и стоимостей должно совпадать")
    if any(weight <= 0 for weight in weights):
        raise ValueError("Все веса должны быть положительными")

    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for current_capacity in range(capacity + 1):
            dp[i][current_capacity] = dp[i - 1][current_capacity]
            if weight <= current_capacity:
                candidate = dp[i - 1][current_capacity - weight] + value
                if candidate > dp[i][current_capacity]:
                    dp[i][current_capacity] = candidate

    chosen_items: list[int] = []
    current_capacity = capacity

    for i in range(n, 0, -1):
        if dp[i][current_capacity] != dp[i - 1][current_capacity]:
            chosen_items.append(i - 1)
            current_capacity -= weights[i - 1]

    chosen_items.reverse()
    return dp[n][capacity], chosen_items


def main() -> None:
    """Демонстрация дискретной задачи о рюкзаке."""
    capacity = 10
    weights = [6, 3, 4, 2]
    values = [30, 14, 16, 9]

    max_value, chosen_items = solve_knapsack(capacity, weights, values)

    print(f"Вместимость рюкзака: {capacity}")
    print(f"Веса предметов: {weights}")
    print(f"Стоимости предметов: {values}")
    print(f"Максимальная стоимость: {max_value}")
    print(f"Выбранные предметы: {chosen_items}")


if __name__ == "__main__":
    main()
