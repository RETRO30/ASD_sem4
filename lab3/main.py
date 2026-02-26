from search import automata
from search import kmp
from search import boyer_mur
from search import rabin_karp


def read_text_from_file(filename):
    """Чтение содержимого текстового файла."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    # Путь к файлу с текстом
    filename = "text.txt"
    # Задаём образец для поиска
    pattern = "ёлочка"   # замените на нужный

    try:
        text = read_text_from_file(filename)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return

    print(f"Текст (первые 100 символов): {text[:100]}...")
    print(f"Образец: '{pattern}'\n")

    # Формируем алфавит для алгоритмов, которым он нужен (автоматный)
    alphabet = set(text) | set(pattern)

    # Автоматный поиск
    auto_pos = automata.search(text, pattern, alphabet)
    print(f"Автоматный поиск: {auto_pos}")

    # КМП
    kmp_pos = kmp.search(text, pattern)
    print(f"КМП: {kmp_pos}")

    # Бойер-Мур
    bm_pos = boyer_mur.search(text, pattern)
    print(f"Бойер-Мур: {bm_pos}")

    # Рабин-Карп
    rk_pos = rabin_karp.search(text, pattern)
    print(f"Рабин-Карп: {rk_pos}")

if __name__ == "__main__":
    main()