"""Tests for tree_tools.count_tips.
Run with:   python3 test_tree.py      (or: pytest -q)
"""
from tree_tools import count_tips


def test_two_tips() -> None:
    """Test tip count fora 2-taxon Newick tree."""
    assert count_tips("(A,B);") == 2


def test_four_tips():
    """Test tip count for a 4 taxon balacned Newick tree."""
    assert count_tips("((A,B),(C,D));") == 4


def test_three_tips():
    assert count_tips("(A,(B,C));") == 3


if __name__ == "__main__":
    test_two_tips()
    test_four_tips()
    test_three_tips()
    print("all tests passed")
