def compute_prefix_function(pattern):
    """Вычисление префикс-функции для образца."""
    m = len(pattern)
    pi = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and pattern[i] != pattern[k]:
            k = pi[k - 1]
        if pattern[i] == pattern[k]:
            k += 1
        pi[i] = k
    return pi

def search(text, pattern):
    """Поиск всех вхождений pattern в text с помощью алгоритма КМП."""
    if not pattern:
        return []
    n, m = len(text), len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0  # количество символов, совпавших в текущем окне
    positions = []
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            positions.append(i - m + 1)
            q = pi[q - 1]
    return positions