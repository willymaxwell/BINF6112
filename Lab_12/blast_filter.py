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
    # Read tab-seperated file with specified column names
    hits = pd.read_csv(path, sep='\t', names=cols)

    # Filter for significant hits (E-value < 1e-5)
    sig = hits[hits['evalue'] < 1e-5]

    # Sort by E-value and take the frist (best) hit for each query
    best = sig.sort_values('evalue').groupby('query').first()

    print(f"significant hits: {len(sig)}")
    for query, row in best.iterrows():
        print(f"{query} -> {row['subject']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main("data/blast.tsv")
