def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Заполнение таблицы динамического программирования
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )

    print('Таблица DP:')
    for row in dp:
        print(row)

    # Восстановление выбранных предметов
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    selected.reverse()
    return dp[n][capacity], selected


# Пример
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, selected_items = knapsack(weights, values, capacity)

print('Максимальная стоимость:', max_value)
print('Выбранные предметы:', selected_items)

for i in selected_items:
    print(f'Предмет {i}: вес = {weights[i]}, стоимость = {values[i]}')
