from typing import Sequence


def pack_into_bins(items: Sequence[int], capacity: int) -> tuple[int, list[list[int]]]:
    """Решает задачу о раскладке по ящикам.

    Теория:
    - Дан набор предметов и ящики одинаковой вместимости.
    - Нужно разложить все предметы так, чтобы число использованных ящиков
      было минимальным.
    - Задача NP-трудная, поэтому для точного решения используется
      поиск с возвратом и отсечения по симметриям.

    Args:
        items: Размеры предметов.
        capacity: Вместимость одного ящика.

    Returns:
        Кортеж `(bins_count, packing)`, где:
        - `bins_count` — минимальное число ящиков,
        - `packing` — список ящиков, каждый ящик содержит размеры предметов.

    Raises:
        ValueError: Если входные данные некорректны.
    """
    if capacity <= 0:
        raise ValueError("Вместимость ящика должна быть положительной")
    if any(item <= 0 for item in items):
        raise ValueError("Размеры предметов должны быть положительными")
    if any(item > capacity for item in items):
        raise ValueError("Предмет не может быть больше вместимости ящика")

    ordered_items = sorted(items, reverse=True)
    best_packing: list[list[int]] | None = None
    bins: list[list[int]] = []
    loads: list[int] = []

    def backtrack(index: int) -> None:
        nonlocal best_packing

        if best_packing is not None and len(bins) >= len(best_packing):
            return

        if index == len(ordered_items):
            best_packing = [box[:] for box in bins]
            return

        item = ordered_items[index]
        seen_loads: set[int] = set()

        for box_index, load in enumerate(loads):
            if load in seen_loads:
                continue
            if load + item > capacity:
                continue

            seen_loads.add(load)
            bins[box_index].append(item)
            loads[box_index] += item
            backtrack(index + 1)
            loads[box_index] -= item
            bins[box_index].pop()

        bins.append([item])
        loads.append(item)
        backtrack(index + 1)
        bins.pop()
        loads.pop()

    backtrack(0)

    if best_packing is None:
        return 0, []
    return len(best_packing), best_packing


def main() -> None:
    """Демонстрация задачи о раскладке по ящикам."""
    items = [4, 8, 1, 4, 2, 1]
    capacity = 10

    bins_count, packing = pack_into_bins(items, capacity)

    print(f"Предметы: {items}")
    print(f"Вместимость ящика: {capacity}")
    print(f"Минимальное число ящиков: {bins_count}")
    print(f"Раскладка по ящикам: {packing}")


if __name__ == "__main__":
    main()
