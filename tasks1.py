def filter_even_squares(numbers: list[int]) -> list[int]:
    """Задача 1 (List comprehensions):
    Верните список квадратов только чётных чисел из переданного списка.
    Пример: [1, 2, 3, 4] -> [4, 16]
    """
    return [x**2 for x in numbers if x % 2 == 0]


def count_words(text: str) -> dict[str, int]:
    """Задача 2 (Строки и словари):
    Приведите текст к нижнему регистру, уберите точки и запятые,
    и верните словарь, где ключ — слово, а значение — сколько раз оно встретилось.
    Пример: "Кот, кот и пес." -> {"кот": 2, "и": 1, "пес": 1}
    """
    s = text.lower().replace(",", "").replace(".", "")
    m = [x for x in s.split() if x != ""]
    d = {}
    for i in m:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def get_unique_ordered(items: list[str]) -> list[str]:
    """Задача 3 (Множества и сохранение порядка):
    Уберите дубликаты из списка, сохранив исходный порядок элементов.
    Пример: ["a", "b", "a", "c", "b"] -> ["a", "b", "c"]
    """
    return list(sorted(set(items)))


def invert_dict(data: dict[str, int]) -> dict[int, str]:
    """Задача 4 (Dict comprehensions):
    Поменяйте ключи и значения словаря местами.
    Пример: {"apple": 1, "banana": 2} -> {1: "apple", 2: "banana"}
    """
    return {value: key for key, value in data.items()}


def safe_divide(a: float, b: float) -> float | None:
    """Задача 5 (Исключения try/except):
    Разделите a на b. Если происходит деление на ноль (ZeroDivisionError),
    верните None вместо падения программы.
    """
    if b != 0:
        return a / b
    return None
