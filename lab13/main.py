def bin_packing_optimal(items, capacity) -> list | None:
    items = sorted(items, reverse=True)
    best_bins = None

    def backtrack(index, bins, loads):
        nonlocal best_bins

        if best_bins is not None and len(bins) >= len(best_bins):
            return

        if index == len(items):
            best_bins = [bin_[:] for bin_ in bins]
            return

        item = items[index]

        used_loads = set()

        for i in range(len(bins)):
            if loads[i] + item <= capacity and loads[i] not in used_loads:
                print(loads[i], item)
                used_loads.add(loads[i])

                bins[i].append(item)
                loads[i] += item

                backtrack(index + 1, bins, loads)

                bins[i].pop()
                loads[i] -= item
        if item <= capacity:
            bins.append([item])
            loads.append(item)

            backtrack(index + 1, bins, loads)

            bins.pop()
            loads.pop()

    backtrack(0, [], [])
    return best_bins


items = [4, 8, 3, 4, 2, 1]
capacity = 10

result = bin_packing_optimal(items, capacity)
if result is None:
    print('Нет решения')
else:
    print('Оптимальное размещение:')
    for i, bin_ in enumerate(result, 1):
        print(f'Ящик {i}: {bin_}, сумма = {sum(bin_)}')

    print('Минимум ящиков:', len(result))
