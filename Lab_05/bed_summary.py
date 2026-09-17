#!/usr/bin/env python3
# LAB 05: REFACTORED SCRIPT
""" --- AI-use disclosure -------------------------------------------------------
AI Tool: Gemini Notebook (Gemini 1.5 Pro)

Purpose: Consulted as a reference for PEP 8 type-hinting conventions and for brainstorming
 unit test cases (verifying 0-based half-open interval calculations and malformed
 line handling). All refactored logic and test execution were independently
 reviewed and verified.

Prompt: "Help refactor bed_summary.py with type hints and suggest edge-case 
test cases for 0-based half-open interval calculations."
 -----------------------------------------------------------------------------"""
import sys
def interval_length(start: int, end: int) -> int:
    """Calculate the length of a 0-based half-open BED interval."""
    # BED intervals are 0-based half-open [start, end), so length is (end - start) without adding 1
    return end - start

def summarize_bed(path: str) -> tuple[int, int]:
    """Parse a BED file and return (interval_count, total_covered_bp)."""
    interval_count = 0
    total_covered_bp = 0

    with open(path, "r", encoding="utf-8") as file_handle:
        for line_num, line in enumerate(file_handle, 1):
            # Skip empty lines and comment lines
            if line.startswith("#") or not line.strip():
                continue

            fields = line.strip().split()

            # Defensive check: ensure line has at least chromosome, start, and end (columns 0, 1, 2)
            if len(fields) < 3:
                print(f"Warning: Skipping malformed line {line_num}: {line.strip()}", file=sys.stderr)
                continue

            try:
                start_coord = int(fields[1])
                end_coord = int(fields[2])
            except ValueError:
                print(f"Warning: Non-integer coordinates on line {line_num}: {line.strip()}", file=sys.stderr)
                continue

            interval_count += 1
            total_covered_bp += interval_length(start_coord, end_coord)

    return interval_count, total_covered_bp


def main(path: str) -> None:
    """Execute BED file summary and print formatted results."""
    interval_count, total_covered_bp = summarize_bed(path)

    print(f"intervals: {interval_count}")
    print(f"total covered bp: {total_covered_bp}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python3 bed_summary.py <path_to_bed>", file=sys.stderr)
        sys.exit(1)

    main(sys.argv[1])
