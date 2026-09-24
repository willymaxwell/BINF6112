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

def calculate_mean_length(rows: list[dict[str, str]]) -> float:
	"""Calculate the mean length of genes from a list of row dictionaries."""
	if not rows:
		return 0.0
	return sum(int(r["length"]) for r in rows) / len(rows)

def main(path):
	"""Orchestrate CSV reading, GC filtering, metric calculation, and output formatting."""
	try:
		rows = read_gene_csv(path)
	except FileNotFoundError:
		print(f"Error: File '{path}' not found.", file=sys.stderr)
		sys.exit(1)
	except (ValueError, KeyError) as err:
		print(f"Error: Invalid or malformed CSV data in '{path}': {err}", file=sys.stderr)
		sys.exit(1)

	if not rows:
		print(f"Warning: No data rows found in '{path}'.", file=sys.stderr)
		return

	try:
		gc_rich_rows = filter_gc_rich(rows)
	except ValueError as err:
		print(f"Error: Non-numeric GC value in CSV: {err}", file=sys.stderr)
		sys.exit(1)

	if not gc_rich_rows:
		print("Warning: No GC-rich genes (> 0.5) found.", file=sys.stderr)
		return

	names = extract_sorted_names(gc_rich_rows)

	try:
		mean_len = calculate_mean_length(gc_rich_rows)
	except ValueError as err:
		print(f"Error: Non-integer length value in CSV: {err}", file=sys.stderr)
		sys.exit(1)

	print(f"GC-rich genes: {', '.join(names)}")
	print(f"mean length of GC-rich genes: {mean_len:.2f}")

if __name__ == "__main__":
	if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
		print("Usage: python3 gene_filter.py <path_to_csv>", file=sys.stderr)
		sys.exit(1)

	main(sys.argv[1])
