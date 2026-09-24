#!/usr/bin/env python3
"""Filter a gene table with comprehensions. Complete each TODO.
Run: python3 gene_filter.py data/genes.csv
"""
import csv
import sys

def read_gene_csv(path: str) -> list[dict[str, str]]:
    """Read and validate a gene CSV file, returning a list of row dictionaries."""
    with open(path, "r", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)

        if not reader.fieldnames or not {"gene", "gc", "length"}.issubset(set(reader.fieldnames)):
            print(f"Error: CSV file '{path}' must contain 'gene', 'gc', and 'length' columns.", file=sys.stderr)
            sys.exit(1)

        return list(reader)

def filter_gc_rich(rows: list[dict[str, str]], threshold: float = 0.5) -> list[dict[str, str]]:
    """Filter rows for genes with GC content strictly greater than the threshold."""
    return [r for r in rows if float(r["gc"]) > threshold]

def extract_sorted_names(rows: list[dict[str, str]]) -> list[str]:
    """Extract and return a sorted list of gene names from rows."""
    return sorted(r["gene"] for r in rows)


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
