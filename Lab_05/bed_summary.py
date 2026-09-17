#!/usr/bin/env python3
# LAB 05: this script WORKS but is messy. REFACTOR it into clean, type-hinted Python
# without changing what it prints:
#   - add type hints to the functions,
#   - use meaningful variable names,
#   - split the work into small, single-purpose functions,
#   - add a module docstring and a comment on the non-obvious line.
# A BED interval is 0-based half-open, so its length is (end - start).
import sys
def go(f):
    x=open(f); n=0; t=0
    for l in x:
        if l.strip()=='':continue
        p=l.split()
        n=n+1
        t=t+(int(p[2])-int(p[1]))
    print('intervals: '+str(n))
    print('total covered bp: '+str(t))
go(sys.argv[1])

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
