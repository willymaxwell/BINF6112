"""tree_tools -- count the tips (leaves) of a Newick tree.

LAB 09: the function below has a BUG. Write tests in test_tree.py, run them, find the
bug, and fix it here.
"""


def count_tips(newick):
    """Return the number of tips (leaf labels) in a Newick tree string."""
    return newick.count(",")     # BUG: this is off by one -- your tests should catch it
