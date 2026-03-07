from typing import Callable


def min_throws_two_eggs(floors: int) -> int:
    """Возвращает минимальное число бросков в худшем случае для 2 яиц.

    Для двух яиц оптимальная стратегия использует убывающие шаги:
    `k, k-1, ..., 1`, где `k` — минимальное число, удовлетворяющее
    `k * (k + 1) / 2 >= floors`.
    """
    if floors < 0:
        raise ValueError("Количество этажей не может быть отрицательным")

    k = 0
    covered = 0
    while covered < floors:
        k += 1
        covered += k
    return k


def find_break_floor_two_eggs(
    floors: int,
    breaks_from: Callable[[int], bool],
) -> tuple[int, int]:
    """Находит пороговый этаж N для 2 яиц.

    Условие:
    - Если бросить яйцо с этажа `N` или выше, оно разобьется.
    - С этажей ниже `N` яйцо не разбивается.

    Args:
        floors: Число этажей в здании.
        breaks_from: Функция-предикат, возвращающая `True`, если яйцо
            разобьется при броске с указанного этажа.

    Returns:
        `(N, throws_count)`, где:
        - `N` — искомый пороговый этаж (1..floors+1),
        - `throws_count` — фактическое число бросков, сделанных алгоритмом.

    Note:
        `N = floors + 1` означает, что яйцо не разбивается ни на одном этаже.
    """
    if floors <= 0:
        raise ValueError("Количество этажей должно быть положительным")

    max_throws = min_throws_two_eggs(floors)
    throws_count = 0

    previous_safe = 0
    current_floor = 0

    # Этап 1: прыжки с уменьшающимся шагом первым яйцом.
    for step in range(max_throws, 0, -1):
        current_floor = min(floors, current_floor + step)
        throws_count += 1

        if breaks_from(current_floor):
            # Этап 2: линейный поиск вторым яйцом.
            for floor in range(previous_safe + 1, current_floor):
                throws_count += 1
                if breaks_from(floor):
                    return floor, throws_count
            return current_floor, throws_count

        previous_safe = current_floor
        if current_floor == floors:
            break

    return floors + 1, throws_count


def main() -> None:
    """Демонстрация задачи о бросании яиц для 100-этажного здания."""
    floors = 100

    # Для примера считаем, что яйцо начинает биться с 73 этажа.
    hidden_n = 73

    def breaks_from(floor: int) -> bool:
        return floor >= hidden_n

    worst_case_throws = min_throws_two_eggs(floors)
    found_n, used_throws = find_break_floor_two_eggs(floors, breaks_from)

    print(f"Этажей в здании: {floors}")
    print(f"Минимум бросков в худшем случае: {worst_case_throws}")
    print(f"Найденный пороговый этаж N: {found_n}")
    print(f"Фактически использовано бросков: {used_throws}")


if __name__ == "__main__":
    main()
