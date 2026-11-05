#!/usr/bin/env python3
"""Filter BLAST tabular hits with pandas. Complete each TODO.
Run: python3 blast_filter.py data/blast.tsv

BLAST -outfmt 6 is tab-separated. Here the columns are:
  query, subject, evalue, pident
"""
import sys
import pandas as pd


def main(path):
    cols = ["query", "subject", "evalue", "pident"]
    # TODO: hits = read the TSV with pd.read_csv (sep tab, names=cols)
    hits =
    # TODO: sig = rows of hits where evalue < 1e-5
    sig =
    # TODO: best = sig sorted by evalue, then groupby("query").first()
    best =
    print(f"significant hits: {len(sig)}")
    for query, row in best.iterrows():
        print(f"{query} -> {row['subject']}")


if __name__ == "__main__":
    main(sys.argv[1])
