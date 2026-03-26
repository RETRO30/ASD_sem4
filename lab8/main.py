from typing import Sequence


def count_change_ways(amount: int, coins: Sequence[int]) -> int:
    """Считает количество способов размена заданной суммы.

    Используется динамическое программирование для подсчета комбинаций
    (порядок монет не важен).

    Идея:
    - `ways[s]` хранит число способов набрать сумму `s`.
    - База: `ways[0] = 1` (один способ набрать ноль — взять ни одной монеты).
    - Для каждого номинала `c` обновляем `ways[s] = ways[s] + ways[s - c]` для `s >= c`.

    Args:
        amount: Целевая сумма (целое неотрицательное число).
        coins: Доступные номиналы монет (положительные целые).

    Returns:
        Количество различных способов набрать `amount`.

    Raises:
        ValueError: Если сумма отрицательна или в номиналах есть неположительные значения.
    """
    if amount < 0:
        raise ValueError("Сумма не может быть отрицательной")

    if any(c <= 0 for c in coins):
        raise ValueError("Номиналы монет должны быть положительными")

    unique_coins = sorted(set(coins))

    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in unique_coins:
        for target in range(coin, amount + 1):
            ways[target] = ways[target] + ways[target - coin]
            print(ways)
        

    return ways[amount]


def main() -> None:
    """Демонстрация задачи размена монет."""
    amount = 5
    coins = [1, 2, 5]

    ways = count_change_ways(amount, coins)

    print(f"Сумма: {amount}")
    print(f"Номиналы: {coins}")
    print(f"Количество способов размена: {ways}")


if __name__ == "__main__":
    main()
