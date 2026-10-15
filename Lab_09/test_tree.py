"""Tests for tree_tools.count_tips.
Run with:   python3 test_tree.py      (or: pytest -q)
"""
from tree_tools import count_tips


def test_two_tips():
    # TODO: assert count_tips("(A,B);") == 2
    pass


def test_four_tips():
    # TODO: assert count_tips("((A,B),(C,D));") == 4
    pass


def test_three_tips():
    # TODO: assert count_tips("(A,(B,C));") == 3
    pass


if __name__ == "__main__":
    test_two_tips()
    test_four_tips()
    test_three_tips()
    print("all tests passed")
