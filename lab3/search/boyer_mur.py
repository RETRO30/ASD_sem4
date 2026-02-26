def build_bad_char_table(pattern, alphabet):
    """Построение таблицы стоп-символов (последнее вхождение символа в образец)."""
    table = {}
    m = len(pattern)
    for c in alphabet:
        table[c] = -1
    for i, c in enumerate(pattern):
        table[c] = i
    return table

def search(text, pattern):
    """Поиск всех вхождений pattern в text с помощью алгоритма Бойера-Мура (эвристика стоп-символа)."""
    if not pattern:
        return []
    n, m = len(text), len(pattern)
    # Для алфавита используем множество символов текста и образца
    alphabet = set(text) | set(pattern)
    bad_char = build_bad_char_table(pattern, alphabet)
    
    positions = []
    i = 0
    while i <= n - m:
        j = m - 1
        # Двигаемся справа налево
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            # Найдено вхождение
            positions.append(i)
            i += 1  # сдвиг на 1
        else:
            # Сдвиг по стоп-символу
            # Индекс последнего вхождения text[i+j] в образец (или -1)
            last = bad_char.get(text[i + j], -1)
            # Сдвиг должен быть как минимум 1, максимум - так, чтобы j-й символ образца встал под last
            shift = max(1, j - last)
            i += shift
    return positions