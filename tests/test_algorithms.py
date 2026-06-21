"""Tests for algorithm modules: selection sort, palindrome, binary conversion."""

import os

import pytest

from tests.conftest import load_classes_from_source, load_module_from_path

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------------------
# Python/selection_sort.py  (bubbleSort - actually selection sort)
# ---------------------------------------------------------------------------
class TestSelectionSort:
    """Tests for the selection sort in Python/selection_sort.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "Python", "selection_sort.py")
        mod = load_module_from_path(path, "selection_sort")
        self.bubbleSort = mod.bubbleSort

    def test_sort_unsorted(self, capsys):
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.bubbleSort(arr)
        assert arr == [11, 12, 22, 25, 34, 64, 90]

    def test_sort_already_sorted(self, capsys):
        arr = [1, 2, 3, 4, 5]
        self.bubbleSort(arr)
        assert arr == [1, 2, 3, 4, 5]

    def test_sort_reverse_sorted(self, capsys):
        arr = [5, 4, 3, 2, 1]
        self.bubbleSort(arr)
        assert arr == [1, 2, 3, 4, 5]

    def test_sort_single_element(self, capsys):
        arr = [42]
        self.bubbleSort(arr)
        assert arr == [42]

    def test_sort_duplicates(self, capsys):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.bubbleSort(arr)
        assert arr == sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

    def test_sort_negative_numbers(self, capsys):
        arr = [-3, -1, -4, -1, -5]
        self.bubbleSort(arr)
        assert arr == [-5, -4, -3, -1, -1]

    def test_sort_mixed_negative_positive(self, capsys):
        arr = [3, -1, 4, -5, 2]
        self.bubbleSort(arr)
        assert arr == [-5, -1, 2, 3, 4]

    def test_sort_empty(self, capsys):
        arr = []
        self.bubbleSort(arr)
        assert arr == []

    def test_sort_two_elements(self, capsys):
        arr = [2, 1]
        self.bubbleSort(arr)
        assert arr == [1, 2]


# ---------------------------------------------------------------------------
# Python/palandrome_recursion.py  (isPalindrome, isPalRec)
# ---------------------------------------------------------------------------
class TestPalindromeRecursion:
    """Tests for palindrome checker in Python/palandrome_recursion.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "Python", "palandrome_recursion.py")
        mod = load_module_from_path(path, "palandrome_recursion")
        self.isPalindrome = mod.isPalindrome
        self.isPalRec = mod.isPalRec

    def test_even_palindrome(self):
        assert self.isPalindrome("geeg") is True

    def test_odd_palindrome(self):
        assert self.isPalindrome("aba") is True

    def test_single_char(self):
        assert self.isPalindrome("a") is True

    def test_empty_string(self):
        assert self.isPalindrome("") is True

    def test_not_palindrome(self):
        assert self.isPalindrome("hello") is False

    def test_two_char_palindrome(self):
        assert self.isPalindrome("aa") is True

    def test_two_char_not_palindrome(self):
        assert self.isPalindrome("ab") is False

    def test_longer_palindrome(self):
        assert self.isPalindrome("racecar") is True

    def test_longer_not_palindrome(self):
        assert self.isPalindrome("python") is False


# ---------------------------------------------------------------------------
# Python/binary_recursioon.py  (find, decToBinary)
# ---------------------------------------------------------------------------
class TestBinaryConversion:
    """Tests for decimal-to-binary in Python/binary_recursioon.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "Python", "binary_recursioon.py")
        mod = load_module_from_path(path, "binary_recursioon")
        self.find = mod.find
        self.decToBinary = mod.decToBinary

    def test_find_25(self):
        assert self.find(25) == 11001

    def test_find_0(self):
        assert self.find(0) == 0

    def test_find_1(self):
        assert self.find(1) == 1

    def test_find_2(self):
        assert self.find(2) == 10

    def test_find_10(self):
        assert self.find(10) == 1010

    def test_find_255(self):
        assert self.find(255) == 11111111

    def test_dec_to_binary_25(self):
        assert self.decToBinary(25) == "11001"

    def test_dec_to_binary_0(self):
        assert self.decToBinary(0) == "0"

    def test_dec_to_binary_1(self):
        assert self.decToBinary(1) == "1"

    def test_dec_to_binary_10(self):
        assert self.decToBinary(10) == "1010"

    def test_dec_to_binary_128(self):
        assert self.decToBinary(128) == "10000000"
