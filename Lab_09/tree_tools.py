"""tree_tools -- count the tips (leaves) of a Newick tree.

LAB 09: the function below has a BUG. Write tests in test_tree.py, run them, find the
bug, and fix it here.
"""


def count_tips(newick: str) -> int:
    """Return the number of tips (leaf labels) in a Newick tree string."""
    if not newick or not newick.strip():
        return 0
    # Strip structural Newick characters: parentheses and trailing semicolon
    cleaned = newick.replace("(", "").replace(")", "").replace(";". "")
    # Split by comma to isolate individual tip labels
    labels = cleaned.split(",")
    # Return count of non empty labels
    return len([x for x in labels if x.strip()])
