def search(text, pattern, base=256, modulus=101):
    """Поиск всех вхождений pattern в text с помощью алгоритма Рабина-Карпа."""
    if not pattern:
        return []
    n, m = len(text), len(pattern)
    if m > n:
        return []

    # Вычисляем хэш образца и первого окна текста
    h_pattern = 0
    h_window = 0
    for i in range(m):
        h_pattern = (h_pattern * base + ord(pattern[i])) % modulus
        h_window = (h_window * base + ord(text[i])) % modulus

    # Предвычисляем значение base^(m-1) % modulus для удаления старшего символа
    power = 1
    for i in range(m - 1):
        power = (power * base) % modulus

    positions = []
    for i in range(n - m + 1):
        if h_pattern == h_window:
            # Если хэши совпали, проверяем посимвольно
            if text[i : i + m] == pattern:
                positions.append(i)

        # Пересчёт хэша для следующего окна (если не последний)
        if i < n - m:
            h_window = (h_window - ord(text[i]) * power) % modulus
            h_window = (h_window * base + ord(text[i + m])) % modulus
            # Приводим к положительному значению
            if h_window < 0:
                h_window += modulus

    return positions
