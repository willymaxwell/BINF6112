#!/usr/bin/env python3
"""Nucleotide composition across all sequences in a FASTA, using NumPy.
Complete each TODO. Run: python3 composition.py data/sequences.fasta
"""
import sys
from typing import List
import numpy as np


def read_bases(path: str) -> List[str]:
    """Return a list of all sequence characters (headers removed, uppercased)."""
    bases = []
    with open(path) as fh:
        for line in fh:
            if not line.startswith(">"):
                bases.extend(line.strip().upper())
    return bases


def main(path: str) -> None:
    """Analyze necleotide frequencies and GC content using NumPy vectorization"""
    arr = np.array(read_bases(path))
    for base in "ACGT":
        count = int(np.sum(arr == base))
        print(f"{base}: {count}")
    gc = float(np.isin(arr, ['G','C']).mean())
    print(f"GC fraction: {gc:.2f}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
