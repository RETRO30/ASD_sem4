def build_automaton(pattern, alphabet):
    """Построение таблицы переходов конечного автомата."""
    m = len(pattern)
    # Таблица переходов: для каждого состояния (0..m) и символа -> следующее состояние
    transition = [{} for _ in range(m + 1)]
    
    for state in range(m + 1):
        for char in alphabet:
            # Определяем следующее состояние для символа char из состояния state
            
            # По умолчанию переход в 0 (начальное состояние)
            next_state = 0
            
            if state < m and char == pattern[state]:
                # Если символ совпадает со следующим символом образца, переходим в state+1
                next_state = state + 1
            else:
                # Ищем максимальную длину префикса, который является суффиксом pattern[:state] + char
                # Перебираем возможные длины от min(state, m) вниз
                for k in range(min(state, m), 0, -1):
                    if pattern[:k] == (pattern[:state] + char)[-k:]:
                        next_state = k
                        break
                # Если ничего не нашли, next_state остается 0
            
            transition[state][char] = next_state
    
    return transition


def search(text, pattern, alphabet):
    """Поиск всех вхождений pattern в text с использованием конечного автомата."""
    if not pattern:
        return []
    transition = build_automaton(pattern, alphabet)
    state = 0
    positions = []
    for i, char in enumerate(text):
        # Если символа нет в алфавите, переходим в состояние 0 (автомат не знает таких символов)
        state = transition[state].get(char, 0)
        if state == len(pattern):
            positions.append(i - len(pattern) + 1)
    return positions
