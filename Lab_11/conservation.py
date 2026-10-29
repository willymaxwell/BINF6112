#!/usr/bin/env python3
"""Per-column conservation of a PHYLIP alignment, using NumPy.
Complete each TODO. Run: python3 conservation.py data/alignment.phy
"""
import sys
import numpy as np


def read_phylip(path):
    """Return a list of sequences (as lists of characters) from a relaxed PHYLIP file."""
    seqs = []
    with open(path) as fh:
        fh.readline()                         # first line: "<n_taxa> <length>"
        for line in fh:
            if not line.strip():
                continue
            name, seq = line.split()
            seqs.append(list(seq))
    return seqs


def main(path):
    mat = np.array(read_phylip(path))
    n, cols = mat.shape
    # TODO: cons = per-column fraction of rows equal to the first row
    #       (compare mat == mat[0], then take the mean over axis 0)
    cons =
    # TODO: conserved = number of columns whose conservation is exactly 1.0 (int)
    conserved =
    # TODO: variable = 1-based positions where cons < 1.0
    #       (np.where(cons < 1.0)[0] + 1, then .tolist())
    variable =
    print(f"alignment: {n} sequences x {cols} columns")
    print(f"fully conserved columns: {conserved}")
    print(f"variable columns (1-based): {variable}")


if __name__ == "__main__":
    main(sys.argv[1])
