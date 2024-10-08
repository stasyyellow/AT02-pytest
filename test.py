import pytest
from main import count_vowels

# Проверка строки, содержащей только гласные
def test_all_vowels():
    assert count_vowels("aeiouAEIOU") == 10

# Проверка строки, не содержащей гласных
def test_no_vowels():
    assert count_vowels("bcdfg") == 0

# Проверка смешанных строк (прописные и строчные буквы)
@pytest.mark.parametrize("input_string, expected_count", [
    ("Hello World!", 3),
    ("PYTHON", 2) #потому что "Y" тоже гласная -_-
])
def test_mixed_string(input_string, expected_count):
    assert count_vowels(input_string) == expected_count