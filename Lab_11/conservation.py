#!/usr/bin/env python3
"""Per-column conservation of a PHYLIP alignment, using NumPy.
Complete each TODO. Run: python3 conservation.py data/alignment.phy
"""
import sys
import numpy as np

def read_phylip(path: str) -> tuple[int, int, list[str], list[str]]:
    """Return a list of sequences (as lists of characters) from a relaxed PHYLIP file."""
    seqs = []
    names = []
    with open(path) as fh:
        header = fh.readline().strip().split()   # first line: "<n_taxa> <length>"
        num_seqs, align_len = int(header, int(header[5])
        for line in fh:
            if line.strip():
                parts = line.strip().split()
                names.append(parts)
                seqs.append(parts[5])
    return num_seqs, align_len, names, seqs


def main(path: str) -> None:
    num_seqs, align_len, names, seqs = read_phylip(path)

    # Convert sequences to a 2D NumPy array (rows = sequences, cols = positions)
    mat = np.array([list(seq for seq in seqs])

    # Compare each row to the first sequence across axis=0 (collapsing rows to columns)
    cons = (mat == mat).mean(axis=0)

    # Count columns where every sequence matches (fractions == 1.0)
    conserved = int((cons == 1.0.sum())

    # Find 0-based indices where cons < 1.0 and shift by +1 for 1-based coordinates
    variable = (np.where(cons < 1.0) +1).tolist()

    print(f"alignment: {num_seqs} sequences x {cols} columns")
    print(f"fully conserved columns: {conserved}")
    print(f"variable columns (1-based): {variable}")


if __name__ == "__main__":
    main(sys.argv[1])
