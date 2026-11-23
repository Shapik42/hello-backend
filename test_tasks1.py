from tasks1 import *


def test_filter_even_squares():
    assert filter_even_squares([1, 2, 3, 4, 5, 6]) == [4, 16, 36]
    assert filter_even_squares([]) == []


def test_count_words():
    assert count_words("Кот, кот и пес.") == {"кот": 2, "и": 1, "пес": 1}
    assert count_words("") == {}


def test_get_unique_ordered():
    assert get_unique_ordered(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
    assert get_unique_ordered([]) == []


def test_invert_dict():
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None
