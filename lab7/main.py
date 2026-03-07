from typing import Sequence


def max_subarray(numbers: Sequence[int]) -> tuple[int, int, int]:
    """Находит непрерывный подмассив с максимальной суммой.

    Используется динамическое программирование:
    `dp[i]` — максимальная сумма подмассива, который обязательно
    заканчивается в позиции `i`.

    Args:
        numbers: Одномерный массив целых чисел.

    Returns:
        Кортеж `(max_sum, start_index, end_index)`, где:
        - `max_sum` — максимальная сумма,
        - `start_index` — индекс начала подмассива,
        - `end_index` — индекс конца подмассива (включительно).

    Raises:
        ValueError: Если входной массив пуст.
    """
    if not numbers:
        raise ValueError("Массив не должен быть пустым")

    n = len(numbers)
    dp = [0] * n
    start_index = [0] * n

    dp[0] = numbers[0]
    start_index[0] = 0

    max_sum = dp[0]
    best_left = 0
    best_right = 0

    for i in range(1, n):
        # Либо продолжаем предыдущий подмассив, либо начинаем новый с i.
        if dp[i - 1] + numbers[i] >= numbers[i]:
            dp[i] = dp[i - 1] + numbers[i]
            start_index[i] = start_index[i - 1]
        else:
            dp[i] = numbers[i]
            start_index[i] = i

        if dp[i] > max_sum:
            max_sum = dp[i]
            best_left = start_index[i]
            best_right = i

    return max_sum, best_left, best_right


def main() -> None:
    """Демонстрация работы задачи о максимальном подмассиве."""
    numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    max_sum, left, right = max_subarray(numbers)
    best_subarray = numbers[left : right + 1]

    print(f"Массив: {numbers}")
    print(f"Максимальная сумма: {max_sum}")
    print(f"Подмассив: {best_subarray}")
    print(f"Границы: [{left}, {right}]")


if __name__ == "__main__":
    main()
