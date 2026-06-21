"""Tests for LeetCode and Interview modules."""

import os

import pytest

from tests.conftest import load_classes_from_source, load_module_from_path

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------------------
# LeetCodeProblems/remove_num _from Array.py  (Solution.removeElement)
# ---------------------------------------------------------------------------
class TestRemoveElement:
    """Tests for Solution.removeElement in LeetCodeProblems."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "LeetCodeProblems", "remove_num _from Array.py")
        mod = load_module_from_path(path, "remove_num_from_array")
        self.Solution = mod.Solution

    def test_basic_case(self):
        sol = self.Solution()
        nums = [3, 2, 2, 3]
        k = sol.removeElement(nums, 3)
        assert k == 2
        assert sorted(nums[:k]) == [2, 2]

    def test_all_same(self):
        sol = self.Solution()
        nums = [1, 1, 1]
        k = sol.removeElement(nums, 1)
        assert k == 0

    def test_none_match(self):
        sol = self.Solution()
        nums = [1, 2, 3]
        k = sol.removeElement(nums, 4)
        assert k == 3
        assert sorted(nums[:k]) == [1, 2, 3]

    def test_empty(self):
        sol = self.Solution()
        nums = []
        k = sol.removeElement(nums, 1)
        assert k == 0

    def test_single_match(self):
        sol = self.Solution()
        nums = [5]
        k = sol.removeElement(nums, 5)
        assert k == 0

    def test_single_no_match(self):
        sol = self.Solution()
        nums = [5]
        k = sol.removeElement(nums, 3)
        assert k == 1
        assert nums[0] == 5

    def test_mixed(self):
        sol = self.Solution()
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        k = sol.removeElement(nums, 2)
        assert k == 5
        assert sorted(nums[:k]) == [0, 0, 1, 3, 4]


# ---------------------------------------------------------------------------
# Interview/code_example_1.py  (solve - LRU Cache)
# ---------------------------------------------------------------------------
class TestLRUCache:
    """Tests for the LRU cache solve() in Interview/code_example_1.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "Interview", "code_example_1.py")
        mod = load_module_from_path(path, "code_example_1")
        self.solve = mod.solve

    def test_basic_put_and_get(self, capsys):
        result = self.solve(2, [
            ["put", 1, 10],
            ["put", 2, 20],
            ["get", 1],
        ])
        assert result == [10]

    def test_get_missing_key(self, capsys):
        result = self.solve(2, [
            ["put", 1, 10],
            ["get", 99],
        ])
        assert result == [-1]

    def test_eviction(self, capsys):
        result = self.solve(2, [
            ["put", 1, 10],
            ["put", 2, 20],
            ["put", 3, 30],
            ["get", 1],
        ])
        # key 1 should be evicted (LRU)
        assert result == [-1]

    def test_capacity_one(self, capsys):
        result = self.solve(1, [
            ["put", 1, 100],
            ["get", 1],
            ["put", 2, 200],
            ["get", 1],
            ["get", 2],
        ])
        assert result[0] == 100
        assert result[1] == -1
        assert result[2] == 200

    def test_only_gets(self, capsys):
        result = self.solve(2, [
            ["get", 1],
            ["get", 2],
        ])
        assert result == [-1, -1]

    def test_overwrite_value(self, capsys):
        result = self.solve(2, [
            ["put", 1, 10],
            ["put", 1, 20],
            ["get", 1],
        ])
        assert result == [20]
