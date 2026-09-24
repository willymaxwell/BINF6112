#!/usr/bin/env python3
"""Filter a gene table with comprehensions. Complete each TODO.
Run: python3 gene_filter.py data/genes.csv
"""
import csv
import sys


def main(path):
    with open(path) as fh:
        rows = list(csv.DictReader(fh))
    # TODO: gc_rich = list of rows where float(row["gc"]) > 0.5   (a comprehension)
    gc_rich =
    # TODO: names = sorted list of the "gene" values in gc_rich   (a comprehension)
    names =
    # TODO: mean_len = mean of int(row["length"]) over gc_rich
    mean_len =
    print(f"GC-rich genes: {', '.join(names)}")
    print(f"mean length of GC-rich genes: {mean_len:.2f}")


if __name__ == "__main__":
    main(sys.argv[1])
