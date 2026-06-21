"""Tests for Data Structure modules: LinkedList, DoublyLinkedList, CircularLinkedList."""

import io
import os
import sys
from unittest.mock import patch

import pytest

from tests.conftest import load_classes_from_source, load_module_from_path

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------------------
# Data Structure/basic.py  (has syntax errors after line 101, use extraction)
# ---------------------------------------------------------------------------
class TestBasicLinkedList:
    """Tests for the LinkedList in Data Structure/basic.py (push, reverse)."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "Data Structure", "basic.py")
        classes = load_classes_from_source(path, ["Node", "LinkedList"])
        self.Node = classes["Node"]
        self.LinkedList = classes["LinkedList"]

    def _to_list(self, ll):
        result = []
        current = ll.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def test_push_single(self):
        ll = self.LinkedList()
        ll.push(10)
        assert self._to_list(ll) == [10]

    def test_push_multiple(self):
        ll = self.LinkedList()
        ll.push(1)
        ll.push(2)
        ll.push(3)
        # push prepends, so order is 3, 2, 1
        assert self._to_list(ll) == [3, 2, 1]

    def test_push_empty_list_head(self):
        ll = self.LinkedList()
        assert ll.head is None
        ll.push(42)
        assert ll.head is not None
        assert ll.head.data == 42

    def test_reverse_empty(self):
        ll = self.LinkedList()
        ll.reverse()
        assert ll.head is None

    def test_reverse_single(self):
        ll = self.LinkedList()
        ll.push(1)
        ll.reverse()
        assert self._to_list(ll) == [1]

    def test_reverse_multiple(self):
        ll = self.LinkedList()
        ll.push(1)
        ll.push(2)
        ll.push(3)
        ll.push(4)
        # Before reverse: 4 -> 3 -> 2 -> 1
        assert self._to_list(ll) == [4, 3, 2, 1]
        ll.reverse()
        # After reverse: 1 -> 2 -> 3 -> 4
        assert self._to_list(ll) == [1, 2, 3, 4]

    def test_reverse_twice_returns_original(self):
        ll = self.LinkedList()
        for val in [5, 4, 3, 2, 1]:
            ll.push(val)
        original = self._to_list(ll)
        ll.reverse()
        ll.reverse()
        assert self._to_list(ll) == original

    def test_print_list(self, capsys):
        ll = self.LinkedList()
        ll.push(1)
        ll.push(2)
        ll.push(3)
        ll.print_list()
        captured = capsys.readouterr()
        assert "3" in captured.out
        assert "2" in captured.out
        assert "1" in captured.out

    def test_node_creation(self):
        node = self.Node(99)
        assert node.data == 99
        assert node.next is None


# ---------------------------------------------------------------------------
# Python/link_list.py  (Linklist with append)
# ---------------------------------------------------------------------------
class TestPythonLinklist:
    """Tests for Linklist in Python/link_list.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "Python", "link_list.py")
        mod = load_module_from_path(path, "python_link_list")
        self.Node = mod.Node
        self.Linklist = mod.Linklist

    def _to_list(self, ll):
        result = []
        current = ll.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def test_append_to_empty(self):
        ll = self.Linklist()
        ll.append(10)
        assert self._to_list(ll) == [10]

    def test_append_multiple(self):
        ll = self.Linklist()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        assert self._to_list(ll) == [10, 20, 30]

    def test_empty_list(self):
        ll = self.Linklist()
        assert ll.head is None
        assert self._to_list(ll) == []

    def test_print_list(self, capsys):
        ll = self.Linklist()
        ll.append(1)
        ll.append(2)
        ll.print_list()
        captured = capsys.readouterr()
        assert "1" in captured.out
        assert "2" in captured.out


# ---------------------------------------------------------------------------
# Python/doubly_linklist.py  (Dll with append, print_forward, print_backward)
# ---------------------------------------------------------------------------
class TestDoublyLinkedList:
    """Tests for Dll in Python/doubly_linklist.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "Python", "doubly_linklist.py")
        mod = load_module_from_path(path, "doubly_linklist")
        self.Node = mod.Node
        self.Dll = mod.Dll

    def _to_list_forward(self, dll):
        result = []
        current = dll.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def _to_list_backward(self, dll):
        result = []
        current = dll.head
        if current is None:
            return result
        while current.next:
            current = current.next
        while current:
            result.append(current.data)
            current = current.prev
        return result

    def test_append_single(self):
        dll = self.Dll()
        dll.append(10)
        assert self._to_list_forward(dll) == [10]

    def test_append_multiple(self):
        dll = self.Dll()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        assert self._to_list_forward(dll) == [10, 20, 30]

    def test_backward_traversal(self):
        dll = self.Dll()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        assert self._to_list_backward(dll) == [30, 20, 10]

    def test_prev_pointers(self):
        dll = self.Dll()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        # head.prev should be None
        assert dll.head.prev is None
        # second node's prev should be head
        assert dll.head.next.prev == dll.head
        # third node's prev should be second
        assert dll.head.next.next.prev == dll.head.next

    def test_empty_dll(self):
        dll = self.Dll()
        assert dll.head is None
        assert self._to_list_forward(dll) == []

    def test_print_forward(self, capsys):
        dll = self.Dll()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        dll.print_forward()
        captured = capsys.readouterr()
        assert "10" in captured.out
        assert "20" in captured.out
        assert "30" in captured.out

    def test_print_backward(self, capsys):
        dll = self.Dll()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        dll.print_backward()
        captured = capsys.readouterr()
        assert "30" in captured.out
        assert "20" in captured.out
        assert "10" in captured.out


# ---------------------------------------------------------------------------
# Python/circular_link_list.py  (CircularLinkedList)
# ---------------------------------------------------------------------------
class TestCircularLinkedList:
    """Tests for CircularLinkedList in Python/circular_link_list.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "Python", "circular_link_list.py")
        mod = load_module_from_path(path, "circular_link_list")
        self.CircularLinkedList = mod.CircularLinkedList

    def _to_list(self, cll):
        result = []
        if cll.head is None:
            return result
        current = cll.head
        while True:
            result.append(current.data)
            current = current.next
            if current == cll.head:
                break
        return result

    def test_append_single(self):
        cll = self.CircularLinkedList()
        cll.append(10)
        assert self._to_list(cll) == [10]
        # Single node's next should point to itself
        assert cll.head.next == cll.head

    def test_append_multiple(self):
        cll = self.CircularLinkedList()
        cll.append(10)
        cll.append(20)
        cll.append(30)
        assert self._to_list(cll) == [10, 20, 30]

    def test_circular_property(self):
        cll = self.CircularLinkedList()
        cll.append(1)
        cll.append(2)
        cll.append(3)
        # Last node's next should point back to head
        current = cll.head
        while current.next != cll.head:
            current = current.next
        assert current.next == cll.head

    def test_empty_list(self):
        cll = self.CircularLinkedList()
        assert cll.head is None
        assert self._to_list(cll) == []

    def test_print_list_empty(self, capsys):
        cll = self.CircularLinkedList()
        cll.print_list()
        captured = capsys.readouterr()
        assert "empty" in captured.out.lower()

    def test_print_list_with_data(self, capsys):
        cll = self.CircularLinkedList()
        cll.append(10)
        cll.append(20)
        cll.append(30)
        cll.print_list()
        captured = capsys.readouterr()
        assert "10" in captured.out
        assert "20" in captured.out
        assert "30" in captured.out
